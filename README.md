# Starred

[![ci](https://github.com/maguowei/starred/actions/workflows/ci.yml/badge.svg)](https://github.com/maguowei/starred/actions/workflows/ci.yml)
[![Upload Python Package](https://github.com/maguowei/starred/actions/workflows/deploy.yml/badge.svg)](https://github.com/maguowei/starred/actions/workflows/deploy.yml)

## Install

```bash

$ pip install starred
$ starred --username maguowei --token=xxxxxxxx --sort > README.md
```

## Usage

```bash
$ starred --help

Usage: starred [OPTIONS]

  GitHub starred

  creating your own Awesome List used GitHub stars!

  example:     starred --username maguowei --token=xxxxxxxx --sort > README.md

Options:
  --username TEXT    GitHub username  [required]
  --token TEXT       GitHub token  [required]
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
- [update awesome-stars every day by GitHub Action](https://github.com/maguowei/awesome-stars/blob/master/.github/workflows/schedules.yml) the example with GitHub Action

## FAQ

1. Generate new token

   link: [Github Personal access tokens](https://github.com/settings/tokens)

2. Install the master branch version

    ```bash
    $ pip install -e git+https://github.com/maguowei/starred#egg=starred
    ```
