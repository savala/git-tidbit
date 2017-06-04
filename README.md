# git-tidbit

[![PyPI version](https://badge.fury.io/py/git-tidbit.svg)](https://pypi.python.org/pypi/git-tidbit)
[![PyPI](https://img.shields.io/pypi/l/git-tidbit.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/git-tidbit)
[![PyPI](https://img.shields.io/pypi/dm/git-tidbit.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/git-tidbit)


Get a tidbit on every commit!

![Example](http://imgur.com/HnNeahT.gif)

Some example tidbits:

```
I'm still waiting for the advent of the computer science groupie.
```
```
TIL Ghostbusters (1984) was suppose to have only 3 main ghostbusters (Dan Aykroyd, Eddie Murphy and John Belushi)
```
```
Like fingerprints, everyone's tongue print is different.
```
```
An expert is a person who avoids the small errors as he sweeps on to the
grand fallacy.
		-- Benjamin Stolberg
```
```
TIL a law was implemented in 1950's Greece whereby head shaving with manual clippers was used as punishment for young people caught by police, such as teddyboys and prostitutes. Obligatory hair clipping was finally abolished in Greece in 1982.
```
```
There is no opinion so absurd that some philosopher will not express it.
		-- Marcus Tullius Cicero, "Ad familiares"
```
```
An electric eel can release a charge powerful enough to start 50 cars.
```
```
A man's house is his castle.
		-- Sir Edward Coke
```
```
A snail breathes through its foot.
```
```
You shouldn't wallow in self-pity.  But it's OK to put your feet in it
and swish them around a little.
		-- Guindon
```
```
Ancient Chinese warriors would show off to their enemies before battle, by juggling.
```

# Install
```
pip install git-tidbit --user
```

You'll want to install this globally for your user (rather than inside a virtual environment)
so any/all git repos can find it's modules.

Once installed, you'll need to run `git init` in your existing repositories to pull in our
post-commit hook. If you'd like to do this for all of your existing repos, use the following:

`find /my/dev/folders -name .git -type d -prune -execdir git init \;`

# Uninstall

Once uninstalled, git-tidbit will clean up after itself. You can double check it's cleanliness by looking at your git config for the `init.templatedir` entry. If your git commits complain, remove the `.git/hooks/post-commit` file.

# Develop

1. Clone the repo

2. `cd git-tidbit && virtualenv venv`

3. `pip install -e .`

4. Add your module to the git_tidbit folder. As long as you implement `get_tidbit` and return a string, things should just work!
 - *You can test your module in isolation using the `if __name__ == "__main__": print get_tidbit()` convention*


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

###### *Try out cowsay!*



