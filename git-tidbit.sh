#!/usr/bin/env bash

git commit "$@"

if [ $? -eq 0 ]; then
  echo "Success your commit worked. Here's your fun fact"
  python git_fact.py
else
fi
