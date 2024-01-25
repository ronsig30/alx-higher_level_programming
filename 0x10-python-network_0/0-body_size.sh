#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Make the request and display the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
