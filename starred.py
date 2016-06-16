from github3 import GitHub


if __name__ == '__main__':
    gh = GitHub()
    stars = gh.iter_starred('maguowei')
    for s in stars:
        print(s)

