Snapple fact repository
=========

Snapple service fetches a random fact from snapple


Usage
------

Try it out!
```
    python snapple_service.py
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
