from github3 import GitHub


desc = '''# starred

## backup

```
python starred.py > README.md

```

## Repositories

'''

if __name__ == '__main__':
    gh = GitHub()
    stars = gh.iter_starred('maguowei')
    print(desc)
    for s in stars:
        #print('*', '[{}]({}) stars: {}, forks: {}, languages: {}, desc: {}'.format(s.full_name, s.html_url, s.stargazers, s.fork_count, s.language, s.description))
        print('*', '[{}]({}) stars: {}, forks: {}, languages: {}'.format(s.full_name, s.html_url, s.stargazers, s.fork_count, s.language))

