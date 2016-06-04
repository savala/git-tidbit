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
    service.get_fact()
```

API
---------
    
| API       | Description                         | Return Type |
|-----------|-------------------------------------|-------------|
| get_fact  | fetches one fact from snapple       | string      |
| get_facts | fetches multiple facts from snapple | [string]    |