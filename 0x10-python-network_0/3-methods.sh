#!/bin/bash

# Use curl to send an OPTIONS request and display the Allow header
curl -s -i -X OPTIONS "$1" | awk '/Allow/ {print $2}'

