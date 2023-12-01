#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
x_request_id = response.headers.get('X-Request-Id')

if x_request_id:
    print(x_request_id)
