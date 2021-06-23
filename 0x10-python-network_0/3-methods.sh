#!/bin/bash
# Displays all available http methods
curl -sI "$1" | awk -F FS": " '/^Allow/{print $2}'
