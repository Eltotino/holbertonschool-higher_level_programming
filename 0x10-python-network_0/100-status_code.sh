#!/bin/bash
#Bash script sending a request to a URL passed as argument, displays only the response status code.
curl -s -o /dev/null -I --write-out "%{http_code}" "$1"
