#!/usr/bin/env bash

git commit "$@"

if [ $? -eq 0 ]; then
  echo "Success! Your commit went through. Here's your fun fact"
  python git_tidbit.py
fi
