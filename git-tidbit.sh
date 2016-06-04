#!/usr/bin/env bash

gitfact() {
    message="${1}"
    git commit -m "${message}" > /dev/null
    # python script.py 
}

if [ $# == 1 ]
then
    gitfact
else
    echo "Error: correct usage is git fact message"
fi
