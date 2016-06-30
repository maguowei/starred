#!/usr/bin/env python3

import click
from github3 import GitHub


desc = '''# Starred


- [Content](#starred)

'''

@click.command()
@click.option('--username', default='maguowei', help='GitHub username')
def starred(username):
    gh = GitHub()
    stars = gh.starred_by(username)
    click.echo(desc)
    repo_dict = {}
    for s in stars:
        language = s.language or 'Others'
        description = s.description or ''
        if language not in repo_dict:
            repo_dict[language] = []
        repo_dict[language].append([s.name, s.html_url, description.encode('utf-8').strip()])
    for language in repo_dict.keys():
        data = '    - [{}](#{})'.format(language, language.lower())
        click.echo(data)
    click.echo('')
    for language in repo_dict:
        click.echo('## %s\n' % language)
        for repo in repo_dict[language]:
            data = '* [{}]({}) - {}'.format(*repo)
            click.echo(data)
        click.echo('')


if __name__ == '__main__':
    starred()
