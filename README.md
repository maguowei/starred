# Starred

[![github workflow](https://github.com/maguowei/starred/workflows/ci/badge.svg)](https://github.com/maguowei/starred/actions)

## Install

```bash

$ pip install starred
$ starred --username maguowei --sort > README.md
```

## Usage

```bash
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
    --message TEXT     commit message
    --version          Show the version and exit.
    --help             Show this message and exit.
```

## Demo

```bash
# automatically create the repository
$ export GITHUB_TOKEN=yourtoken
$ starred --username yourname --repository awesome-stars --sort
```

- [`maguowei/awesome-stars`](https://github.com/maguowei/awesome-stars)

## FAQ

1. Generate new token

   link: [Github Personal access tokens](https://github.com/settings/tokens)

2. Why do I need a token?

   -  For unauthenticated requests, the rate limit is 60 requests per
      hour.
      see [Github Api Rate
      Limiting](https://developer.github.com/v3/#rate-limiting)
   -  The token must be passed together when you want to automatically
      create the repository.

3. Install the master branch version

    ```bash
    $ pip install -e git+https://github.com/maguowei/starred#egg=starred
    ```
