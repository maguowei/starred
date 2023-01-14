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

  creating your own Awesome List by GitHub stars!

  example:     starred --username maguowei --token=xxxxxxxx --sort > README.md

Options:
  --username TEXT        GitHub username  [required]
  --token TEXT           GitHub token  [required]
  --sort                 sort by category[language/topic] name alphabetically
                         [default: False]

  --topic                category by topic, default is category by language
                         [default: False]

  --topic_limit INTEGER  topic stargazer_count gt number, set bigger to reduce
                         topics number  [default: 500]

  --repository TEXT      repository name  [default: ]
  --filename TEXT        file name  [default: README.md]
  --message TEXT         commit message  [default: update stars]
  --private              include private repos  [default: False]
  --version              Show the version and exit.
  --help                 Show this message and exit.
```

## Demo

```bash
# automatically create the repository
$ export GITHUB_TOKEN=yourtoken
$ starred --username yourname --repository awesome-stars --sort
```

- [`maguowei/awesome-stars`](https://github.com/maguowei/awesome-stars)
- [update awesome-stars every day by GitHub Action](https://github.com/maguowei/awesome-stars/blob/master/.github/workflows/schedules.yml) the example with GitHub Action

### Who uses starred?

- by search: https://github.com/search?p=1&q=%22Generated+by+starred%22&type=Code
- by topics:
  - https://github.com/topics/starred
  - https://github.com/topics/awesome-stars

## Use [awesome-stars](https://github.com/maguowei/awesome-stars) as template

The simple way to create an awesome-stars repository is to use [maguowei/awesome-stars](https://github.com/maguowei/awesome-stars/generate) as template.
It will auto update your awesome-stars repository every day by GitHub Action.

1. Click [Create a new repository from awesome-stars](https://github.com/maguowei/awesome-stars/generate)

![use-awesome-stars-as-template](https://raw.githubusercontent.com/maguowei/starred/master/imgs/use-awesome-stars-as-template.png)

2. [Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)

set permissions to `Read and write permissions` and click `Save` button

![workflow-permissions](https://raw.githubusercontent.com/maguowei/starred/master/imgs/workflow-permissions.png)

3. Run the workflow first time

click `Run workflow` button

![run-workflow](https://raw.githubusercontent.com/maguowei/starred/master/imgs/run-workflow.png)

4. Customize the workflow schedule

- [.github/workflows/schedules.yml#L5](https://github.com/maguowei/awesome-stars/blob/master/.github/workflows/schedules.yml#L5)

![schedule](https://raw.githubusercontent.com/maguowei/starred/master/imgs/schedule.png)

## FAQ

1. Generate new token

   link: [Github Personal access tokens](https://github.com/settings/tokens)

2. Install the master branch version

    ```bash
    $ poetry build 
    $ pip install dist/starred-${x.x.x}.tar.gz
    ```
3. Dev & Run
   ```bash
   poetry run starred --help
   ```