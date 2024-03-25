import json
from datetime import datetime

def time_difference(d1, d2, unit='hours'):
    d1 = datetime.strptime(d1, '%Y-%m-%dT%H:%M:%SZ')
    d2 = datetime.strptime(d2, '%Y-%m-%dT%H:%M:%SZ')
    
    time_diff = d2 - d1
    
    if unit == 'hours':
        return time_diff.total_seconds() / 3600
    elif unit == 'minutes':
        return time_diff.total_seconds() / 60
    else:
        raise ValueError("Invalid unit. Please use 'hours' or 'minutes'.")

f1 = open("data/4_collaborators_and_users_with_timezone.json")
f2 = open("data/4_pull_requests.json")
data_tz = json.load(f1)
data_pr = json.load(f2)

repos = []

for item in data_pr:
    print(f"repo name of pr is {item['full_name']}")
    pull_requests = []

    for entry in item['pull_requests']:
        if (entry['created_at'] and entry['merged_at']) is not None:
            pull_requests.append(time_difference(entry['created_at'], entry['merged_at'],'hours'))
    if len(pull_requests) > 0:
        average_pull_requests = sum(pull_requests) / len(pull_requests)
    
    repos.append({
        "repo_name": item['full_name'],
        "pull_requests": pull_requests,
        "pull_request_average": average_pull_requests
    })

print(len(repos))

pull_requests_final = []
pull_requests_final.extend(repos['pull_requests'])
average_pr = []
average_pr.extend(repos['pull_request_average'])
with open("timezones2.json", "w") as outfile:
    json.dump(repos, outfile)
print("done writing to json")

final_repos = []
i = 0
for item in data_tz:
    print(f"repo name is {item['name']}")
    locations = []
    for entry in item['users_location']:
        if 'bot' not in entry['login']:
            if entry['location'] is not None:
                locations.append(entry['location'])
            elif entry['bio'] is not None:
                locations.append(entry['bio'])
                #print("biooooooooooooooooooooooooooooooooooo")
            elif entry['company'] is not None:
                #print("companyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                locations.append(entry['company'])

    final_repos.append({
        "repo_name": item['name'],
        "nr_locations": locations,
        "pull_requests2": pull_requests_final[i],
        "pull_request_average": average_pr[i]
    })
    i += 1

with open("timezones.json", "w") as outfile:
    json.dump(final_repos, outfile)
print("done writing to json")