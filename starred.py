#!/usr/bin/env python3

import click
from github3 import GitHub


desc = '''# starred

## backup

```
python starred.py > README.md

```

## Repositories

'''


@click.command()
@click.option('--username', default='maguowei', help='GitHub username')
def starred(username):
    gh = GitHub()
    stars = gh.starred_by(username)
    click.echo(desc)
    for s in stars:
        keys = (s.full_name, s.html_url, s.stargazers_count, s.fork_count, s.language)
        data = '* [{}]({}) stars: {}, forks: {}, languages: {}'.format(*keys)
        click.echo(data)

if __name__ == '__main__':
    starred()
