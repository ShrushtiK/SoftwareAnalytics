import requests
import json

_TOKEN = 'your_token'

#get the users and their location
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

# retrieve all collaborators of a repository        
def get_collaborators(repo_name, token, per_page, page):
    print("get_collabs")
    url = f'https://api.github.com/repos/{repo_name}/contributors?per_page={per_page}&page={page}'
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
            user_info, location = get_user_location(collaborator["login"], token)
            users.append(user_info)
            if location is True:
                location_percentage = location_percentage + 1
        final_location_percentage = location_percentage / len(collaborators)
        print(f"*************Location percentage***********, {final_location_percentage}")

        # Check if there is a next page
        next_page_url = None
        link_header = response.headers.get('Link')
        if link_header:
            links = link_header.split(', ')
            for link in links:
                url, rel = link.split('; ')
                if rel == 'rel="next"':
                    next_page_url = url.strip('<>')

        if location_percentage/len(collaborators) > 0.5:
            return collaborators, users, final_location_percentage, next_page_url
        else:
            return None, None, False, None
    else:
        print(f"Error for collaborators: {response.status_code} {response.reason}")
        return None, None, None, next_page_url
    
# retrieve all commits of a repository    
def get_number_commits(repo_name, token, per_page, page):
    print("get_commits")
    url = f'https://api.github.com/repos/{repo_name}/commits?per_page={per_page}&page={page}'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        commit_count = len(commits)

        # Check if there is a next page
        next_page_url = None
        link_header = response.headers.get('Link')
        if link_header:
            links = link_header.split(', ')
            for link in links:
                url, rel = link.split('; ')
                if rel == 'rel="next"':
                    next_page_url = url.strip('<>')

        return commits, commit_count, next_page_url
    else:
        print(f"Error for number of commits: {response.status_code} {response.reason}")
        return None, None, None

def get_repositories(token, per_page):
    print("get_repos")
    cnt = 0
    search_url = 'https://api.github.com/search/repositories'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'  # Replace with your personal access token
    }
    query = 'tensorflow AND keras AND pytorch AND python'
    params = {
        'q': query,
        'per_page': 99,  # Maximum number of results per page
        'page': 1  # Initial page number
    }
    repositories = []
    while True:
        response = requests.get(search_url, headers=headers, params=params)
        if len(repositories) > 100:
            print("did this actually happen?")
            return repositories
        if response.status_code == 200:
            data=response.json()
            new_repos=[repo for repo in data['items']]
            for repo in new_repos:
                commit_page = 1
                repo_commit_count = 0
                repo_commits = []
                #loop through all pages of commits
                while True:
                    commits, commit_count, next_page = get_number_commits(repo["full_name"],token,per_page,commit_page)
                    print(f'Commit Currently on page {commit_page}')
                    repo_commits.extend(commits)
                    repo_commit_count += commit_count
                    if next_page:
                        commit_page += 1
                    else:
                        break

                if repo_commit_count < 100000 and repo_commit_count > 1000:
                    print(f"Matches commit criteria: {repo['full_name']} {repo_commit_count}")
                    repo_collaborators = []
                    repo_users = []
                    collab_page = 1
                    location_majority = 0
                    #loop through all pages of collaborators & users
                    while True:
                        collaborators, users, loc_majority, next_page = get_collaborators(repo["full_name"], token, per_page,collab_page)
                        print(f'Collaborator Currently on page {collab_page}')
                        if collaborators is not None:
                            repo_collaborators.extend(collaborators)
                            repo_users.extend(users)
                            location_majority += loc_majority
                        if next_page:
                            collab_page += 1
                        else:
                            break
                    location_majority /= collab_page

                    if location_majority > 0.49:
                        print(f"Matches mmajority criteria:  {repo['full_name']} {repo_commit_count}")
                        repositories.append({ "name": repo["full_name"], "commits": repo_commits, "collaborators": repo_collaborators, "users": repo_users})
                        #cnt += 1
                        #if cnt == 3:
                            #for repo in repositories:
                            #    print(repo['name'])
                            #return repositories
                else:
                    print(f"Commit size not met with # commits = {repo_commit_count} for {repo['full_name']}")
            if 'next' in response.links:
                    params['page'] += 1
            else:
                break
        else:
            print(f"Error for get repositories: {response.status_code, response.reason}")
            break

    for repo in repositories:
        print(repo['name'])
    return repositories
                    
if __name__ == "__main__":
    per_page = 99
    repositories = get_repositories(_TOKEN,per_page)
    with open("repositories.json", 'w') as file:
        json.dump(repositories, file)