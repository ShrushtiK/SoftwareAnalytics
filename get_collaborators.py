import requests
import json
import time 

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
        
        return collaborators, users, final_location_percentage, next_page_url
    else:
        print(f"Error for collaborators: {response.status_code} {response.reason}")
        return None, None, None, None, next_page_url
        


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
    
                    
if __name__ == "__main__":
    start_time = time.time()
    repo_name = "BVLC/caffe"
    per_page = 99
    all_collaborators = []
    all_users = []
    all_commits = []
    all_commit_count = 0
    location_percentage = 0
    page = 1

    #loop through all pages of collaborators & users
    while True:
        collaborators, users, loc_percentage, next_page = get_collaborators(repo_name, _TOKEN, per_page, page)
        print(f'Collaborator Currently on page {page}')
        all_collaborators.extend(collaborators)
        all_users.extend(users)
        location_percentage += loc_percentage
        
        if next_page:
            page += 1
        else:
            break
    
    location_percentage /= page
    page = 1

    #loop through all pages of commits
    while True:
        commits, commit_count, next_page = get_number_commits(repo_name,_TOKEN,per_page,page)
        print(f'Commit Currently on page {page}')
        all_commits.extend(commits)
        all_commit_count += commit_count

        if next_page:
            page += 1
        else:
            break

    print(f'$$$$ Number of commits for {repo_name} is {all_commit_count}')
    repository = {
        "name": repo_name,
        "commits": all_commits,
        "collaborators": all_collaborators,
        "users": all_users
    }

    end_time = time.time()
    elapsed_time = end_time - start_time

    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    
    print(f"Program completed in {hours} hours, {minutes} minutes, and {seconds} seconds")
    print(f"##### Location percentage of {repo_name} is {location_percentage}")
    print(f'$$$$ Number of commits for {repo_name} is {all_commit_count}')
    
    output_file = repo_name.replace("/", "_") + ".json"
    with open(output_file, 'w') as file:
        json.dump(repository, file)