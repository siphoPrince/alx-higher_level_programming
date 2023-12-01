#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print("    - type:", type(content))
print("    - content:", content)
print("    - utf8 content:", utf8_content)
