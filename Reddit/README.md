Reddit TIL repository
=========

Reddit service fetches a random TIL (Today I learned) from snapple


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
