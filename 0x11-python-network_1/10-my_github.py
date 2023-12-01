#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]
url = "https://api.github.com/user"

# Use Basic Authentication with username and personal access token as password
response = requests.get(url, auth=(username, token))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
else:
    print(None)
