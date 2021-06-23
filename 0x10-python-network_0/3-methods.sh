#!/bin/bash
# Displays all available http methods
curl -sI "$1" | sed -n 's/Allow: //p'
