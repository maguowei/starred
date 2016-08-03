# Starred

[![Build Status](https://travis-ci.org/maguowei/starred.svg?branch=master)](https://travis-ci.org/maguowei/starred)
[![Requirements Status](https://requires.io/github/maguowei/starred/requirements.svg?branch=master)](https://requires.io/github/maguowei/starred/requirements/?branch=master)


## Install
```
$ pip install starred
$ starred --username maguowei --sort > README.md
```

## Usage
```
$ starred --help

Usage: starred [OPTIONS]

  GitHub starred

  creating your own Awesome List used GitHub stars!

  example:     starred --username maguowei --sort > README.md

Options:
  --username TEXT    GitHub username
  --token TEXT       GitHub token
  --sort             sort by language
  --repository TEXT  repository name
  --version          Show the version and exit.
  --help             Show this message and exit.
```


## Demo

```bash
export GITHUB_TOKEN=yourtoken
# automatically create the repository
starred --username yourusername --repository awesome-stars --sort
```
* [awesome-stars](https://github.com/maguowei/awesome-stars)


## FAQ

1. Generate new token

    goto [Personal access tokens](https://github.com/settings/tokens)

2. Why do I need a token?

    * For unauthenticated requests, the rate limit is 60 requests per hour. 
    see [Rate Limiting](https://developer.github.com/v3/#rate-limiting)
    * The token must be passed together when you want to automatically create the repository.
