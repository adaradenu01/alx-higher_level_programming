#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

try:
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
except (urllib.error.URLError, IndexError) as e:
    print(e)
