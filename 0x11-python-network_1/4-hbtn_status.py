#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

url = 'https://alx-intranet.hbtn.io/status'
try:
    reply = requests.get(url)

    print('Body response:')
    print('\t- type:', type(reply.text))
    print('\t- content:', reply.text)
except Exception as e:
    print(f"Error: {e}")

