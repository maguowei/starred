#!/usr/bin/env python

import os
from collections import OrderedDict
import click
from github3 import GitHub


desc = '''# Starred


- [Content](#starred)

'''


@click.command()
@click.option('--username', default=lambda: os.environ.get('USER', ''), help='GitHub username')
@click.option('--sort',  is_flag=True, help='sort by language')
def starred(username, sort):
    """GitHub starred

    make your own awesome lists page by GitHub star!

    example:
        starred --username maguowei --sort > README.md

    """
    gh = GitHub()
    stars = gh.starred_by(username)
    click.echo(desc)
    repo_dict = {}

    for s in stars:
        language = s.language or 'Others'
        description = s.description or ''

        if language not in repo_dict:
            repo_dict[language] = []

        repo_dict[language].append([s.name, s.html_url, description.strip()])

    if sort:
        repo_dict = OrderedDict(sorted(repo_dict.items(), key=lambda l: l[0]))

    for language in repo_dict.keys():
        data = u'    - [{}](#{})'.format(language, language.lower())
        click.echo(data)
    click.echo('')

    for language in repo_dict:
        click.echo('## %s\n' % language)
        for repo in repo_dict[language]:
            data = u'* [{}]({}) - {}'.format(*repo)
            click.echo(data)
        click.echo('')


if __name__ == '__main__':
    starred()
