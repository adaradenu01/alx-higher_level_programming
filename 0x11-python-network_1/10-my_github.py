#!/usr/bin/python3
"""script that prints user id fom GitHub"""

if __name__ == "__main__":
    import requests
    import sys

username, password = sys.argv[1], sys.argv[2]
url = "https://api.github.com/user"

try:
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    print(f"{response.json()['id']}")
except Exception as e:
    print(f"Error: {e}")
