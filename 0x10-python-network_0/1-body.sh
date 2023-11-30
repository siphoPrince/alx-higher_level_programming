#!/usr/bin/bash

# takes in a URL, sends a GET request to the URL, and displays the body of the response

curl -sLGET "$1" | sed -n '/^HTTP\/1.1 200 OK/,$p' | tail -n +2
