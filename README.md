# git-tidbit
Git a tidbit everytime you successfully commit to a repo.

![Showcase](https://github.com/savala/git-tidbit/blob/master/screenshots/screenshot.png)

#Install
```
pip install git-tidbit
```

Once installed, you'll need to run `git init` in your existing repositories to pull in our
post-commit hook. If you'd like to do this for all of your existing repos, use the following:

`find /my/dev/folders -name .git -type d -prune -execdir git init \;`

#Uninstall

Once uninstalled, git-tidbit will clean up after itself.

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


### Reddit

Reddit TIL repository
=========

Reddit service fetches a random TIL (Today I learned)


Usage
------

Try it out!
```
    python reddit_service.py
```

Returns:
```
    TIL of James Allen, a highwayman who upon his death requested that a copy of his memoir be bound in his skin and given to John Fenno Jr., the man who put him in jail after trying to rob him. According to Allen it was meant as a token of his respect to the man who fought back and stood up to him.
```

Integrate it!
```
    service = SnappleFactService()
    service.get_tidbit()
```

API
---------

| API         | Description                         | Return Type |
|-------------|-------------------------------------|-------------|
| get_tidbit  | fetches one TIL from reddit         | string      |
| get_tidbits | fetches multiple tils from snapple  | [string]    |

Libraries
-----------

```
import urllib2
import json
```

### Snapple

Snapple fact repository
=========

Snapple service fetches a random fact from snapple


Usage
------

Try it out!
```
    python snapple_service.py
```

Returns
```
    The woodpecker can hammer wood up to 16 times per second.
```
Integrate it!
```
    service = SnappleFactService()
    service.get_tidbit()
```

API
---------

| API       | Description                         | Return Type |
|-----------|-------------------------------------|-------------|
| get_tidbit  | fetches one fact from snapple       | string      |
| get_tidbits | fetches multiple facts from snapple | [string]    |

Libraries
-----------

```
from bs4 import BeautifulSoup
import urllib2
```

