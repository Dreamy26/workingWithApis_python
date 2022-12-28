import requests 

# url of the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# the version of the API 
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers) # request to make the call to API
print(f"Status code: {r.status_code}") # print status_code, to make sure the call went through

# Variable that stores API response
response_dict = r.json()

# Prints total number of python repositories on GitHub
print(f"Total repositories: {response_dict['total_count']}")

# Receive information about the repositories & store a list of dictionaries
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Where the first repository is examined. 
# print the number of Keys, to verify how much information is there
repo_dict = repo_dicts[0]
# will print all included dictKeys
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
    
# PULL some values from the keys
print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}") 
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")