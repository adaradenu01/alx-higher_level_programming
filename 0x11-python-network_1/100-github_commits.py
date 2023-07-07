#!/usr/bin/python3
"""
Get the 10 most recent commits from the repository specified on
the command line ordered most recent to oldest in the
format: `<sha>: <author name>`
"""

if __name__ == "__main__":
    import requests
    import sys

repo_name, owner_name = sys.argv[1], sys.argv[2]
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
params = {"author": owner_name, "per_page": 10}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    for commit in response.json():
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
