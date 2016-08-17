# git-tidbit

[![PyPI version](https://badge.fury.io/py/git-tidbit.svg)](https://pypi.python.org/pypi/git-tidbit)
[![PyPI](https://img.shields.io/pypi/l/git-tidbit.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/git-tidbit)
[![PyPI](https://img.shields.io/pypi/dm/git-tidbit.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/git-tidbit)


Get a tidbit on every commit!

![Example](http://imgur.com/HnNeahT.gif)

#Install
```
pip install git-tidbit --user
```

You'll want to install this globally for your user (rather than inside a virtual environment)
so any/all git repos can find it's modules.

Once installed, you'll need to run `git init` in your existing repositories to pull in our
post-commit hook. If you'd like to do this for all of your existing repos, use the following:

`find /my/dev/folders -name .git -type d -prune -execdir git init \;`

#Uninstall

Once uninstalled, git-tidbit will clean up after itself. You can double check it's cleanliness by looking at your git config for the `init.templatedir` entry. If your git commits complain, remove the `.git/hooks/post-commit` file.

#Develop

1. Clone the repo

2. `cd git-tidbit && virtualenv venv`

3. `pip install -e .`


# Usage

Use your normal git workflow. Whenever you commit, you'll learn something new!

```sh
git commit -m "I'm really just doing this to get a snapple fact"
git commit --amend
```

# Tidbit Sources

All tidbit modules **must** implement a `get_tidbit` function
that returns a string. They are free to implement that functionality however they please

## Reddit
Reddit service fetches a random TIL (Today I learned)

## Snapple
Random snapple cap fact

## Fortune

You'll need `fortune` installed. You can get it with your favorite package manager:

```
brew install fortune
yum install fortune-mod
apt-get install fortune fortune-mod
pacman -S fortune-mod
```

####### *Try out cowsay!*



