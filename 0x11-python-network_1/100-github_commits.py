#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./100-github_commits.py <repository> <owner>")
    sys.exit(1)

repository = sys.argv[1]
owner = sys.argv[2]
url = f"https://api.github.com/repos/{owner}/{repository}/commits"

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]  # Take the first 10 commits
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Error:", response.status_code)
