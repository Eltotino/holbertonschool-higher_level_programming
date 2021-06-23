#!/bin/bash
# Displays all available http methods
curl -sI "$1" | awk -v FS": " '/^Allow/{print $2}'
