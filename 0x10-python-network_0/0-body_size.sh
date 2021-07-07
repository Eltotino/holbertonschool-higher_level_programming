#!/bin/bash
#Display length of the sought response
curl -sI "$1" | awk -v FS=": " '/^Content-Length/{print $2}'
