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
  --private          include private repos
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

## Use [awesome-stars](https://github.com/maguowei/awesome-stars) as Template

1. Click [Create a new repository from awesome-stars](https://github.com/maguowei/awesome-stars/generate)

![use-awesome-stars-as-template](imgs/use-awesome-stars-as-template.png)

2. [Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)

set permissions to `Read and write permissions` and click `Save` button

![workflow-permissions](imgs/workflow-permissions.png)

3. Run the workflow first time

click `Run workflow` button

![run-workflow](imgs/run-workflow.png)

4. Customize the workflow schedule

- [.github/workflows/schedules.yml#L5](https://github.com/maguowei/awesome-stars/blob/master/.github/workflows/schedules.yml#L5)

![schedule](imgs/schedule.png)

## FAQ

1. Generate new token

   link: [Github Personal access tokens](https://github.com/settings/tokens)

2. Install the master branch version

    ```bash
    $ pip install -e git+https://github.com/maguowei/starred#egg=starred
    ```
