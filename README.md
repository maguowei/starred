# Starred

[![Build Status](https://travis-ci.org/maguowei/starred.svg?branch=master)](https://travis-ci.org/maguowei/starred)
[![Requirements Status](https://requires.io/github/maguowei/starred/requirements.svg?branch=master)](https://requires.io/github/maguowei/starred/requirements/?branch=master)

```bash
# install and use
pip install starred
starred --username maguowei --sort > README.md
```


## Demo
* [awesome-stars](https://github.com/maguowei/awesome-stars)


## FAQ

1. Generate new token

    goto [Personal access tokens](https://github.com/settings/tokens)

2. When I need a token?
    * For unauthenticated requests, the rate limit is 60 requests per hour. 
    see [Rate Limiting](https://developer.github.com/v3/#rate-limiting)
    * The token must be passed together when you want to automatically create the repository.
