#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys
    
url, email = sys.argv[1], sys.argv[2]
try:
    response = requests.post(url, data={'email': email})
    print(response.text)
except Exception as e:
    print(e)