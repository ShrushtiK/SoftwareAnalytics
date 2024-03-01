import requests
import json

_TOKEN = 'your_token'

def get_user_location(username, token):
    print("get_users")
    url = f'https://api.github.com/users/{username}'
    location = False
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        user_info = response.json()
        location = True if user_info["location"] != None else False
        return user_info, location
    else:
        print(f"Error fetching information for user {username}: {response.status_code} {response.reason}")
        return None, location

def get_collaborators(repo_name, token):
    print("get_collabs")
    url = f'https://api.github.com/repos/{repo_name}/contributors'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        collaborators = response.json()
        location_percentage = 0
        users = []
        for collaborator in collaborators:
            user_info, location =  get_user_location(collaborator["login"], token)
            users.append(user_info)
            if location is True:
                location_percentage = location_percentage + 1
        print(f"*************Location percentage***********, {location_percentage/len(collaborators)}")
        if location_percentage/len(collaborators) > 0.5:
            return collaborators, users, True
        else:
            return None, None, False
    else:
        print(f"Error for collaborators: {response.status_code} {response.reason}")
        


def get_number_commits(repo_name, token):
    print("get_commits")
    url = f'https://api.github.com/repos/{repo_name}/commits'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        commit_count = len(commits)
        return commits, commit_count
    else:
        print(f"Error for number of commits: {response.status_code} {response.reason}")
        return None, None

def get_repositories(token):
    print("get_repos")
    search_url = 'https://api.github.com/search/repositories'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'  # Replace with your personal access token
    }
    query = 'tensorflow AND keras AND pytorch AND python'
    params = {
        'q': query,
        'per_page': 100,  # Maximum number of results per page
        'page': 1  # Initial page number
    }
    repositories = []
    while True:
        response = requests.get(search_url, headers=headers, params=params)
        if len(repositories) > 2:
            return repositories
        if response.status_code == 200:
            data=response.json()
            new_repos=[repo for repo in data['items']]
            for repo in new_repos:
                commits, no_commits = get_number_commits(repo["full_name"], token)
                if no_commits < 100000 and no_commits > 1000:
                    print(f"Matches commit criteria: {repo['full_name']} {no_commits}")
                    collaborators, users, location_majority = get_collaborators(repo["full_name"], token)
                    if location_majority is True:
                        print(f"Matches mmajority criteria:  {repo['full_name']} {no_commits}")
                        repositories.append({ "name": repo["full_name"], "commits": commits, "collaborators": collaborators, "users": users})
                else:
                    print(f"Commit size not met with # comments = {no_commits} for {repo['full_name']}")
            if 'next' in response.links:
                    params['page'] += 1
            else:
                break
        else:
            print(f"Error for get repositories: {response.status_code, response.reason}")
            break
    return repositories
                    
if __name__ == "__main__":
    repositories = get_repositories(_TOKEN)
    with open("repositories.json", 'w') as file:
        json.dump(repositories, file)