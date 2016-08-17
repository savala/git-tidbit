# git-tidbit

Git a tidbit everytime you successfully commit to a repo.

![Showcase](https://github.com/savala/git-tidbit/blob/master/screenshots/screenshot.png)

#Install
```
pip install git-tidbit
```

*If you have trouble on OS X due to permissions, try out `pip install --user git-tidbit`

Once installed, you'll need to run `git init` in your existing repositories to pull in our
post-commit hook. If you'd like to do this for all of your existing repos, use the following:

`find /my/dev/folders -name .git -type d -prune -execdir git init \;`

#Uninstall

Once uninstalled, git-tidbit will clean up after itself. You can double check it's cleanliness by looking at your git config for the `init.templatedir` entry.

#Develop

1. Clone the repo

2.
```sh
git clone https://github.com/savala/git-tidbit.git
```

3.
```sh
sudo pip install -e ./git-tidbit
```


# Usage

Use your normal git workflow. Whenever you commit, you'll learn something new!

```sh
git commit -m "I'm really just doing this to get a snapple fact"
```

# Tidbit Sources

All tidbit modules **must** implement a `get_tidbit` function
that returns a string. They are free to implement that functionality however they please~

## Reddit
Reddit service fetches a random TIL (Today I learned)

## Snapple
Random snapple cap fact

## Fortune

You'll need `fortune` installed. You can get it with your favorite package manager:

```
brew install fortune
yum install fortune
apt-get install fortune fortune-mod
pacman -S fortune-mod
```

####### *Try out cowsay!*



