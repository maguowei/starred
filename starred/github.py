import requests

DEFAULT_QUERY = """
{{
  user(login: "{username}") {{
    starredRepositories(first: 100, after: "{after}", orderBy: {{direction: DESC, field: STARRED_AT}}) {{
      totalCount
      nodes {{
        name
        nameWithOwner
        description
        url
        stargazerCount
        forkCount
        isPrivate
        pushedAt
        updatedAt
        languages(first: 1, orderBy: {{field: SIZE, direction: DESC}}) {{
          edges {{
            node {{
              id
              name
            }}
          }}
        }}
      }}
      pageInfo {{
        endCursor
        hasNextPage
      }}
    }}
  }}
}}
"""


class Repository:
    def __init__(self, name, description, language, url, stargazer_count, is_private):
        self.name = name
        self.description = description
        self.language = language
        self.url = url
        self.stargazer_count = stargazer_count
        self.is_private = is_private


def get_user_starred_by_username(token, username, query=None):
    items = []
    headers = {"Authorization": f"Bearer {token}"}
    if query is None:
        query = DEFAULT_QUERY.format(username=username, after='')
    r = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if r.status_code != 200:
        raise Exception(f'Query failed to run by returning code: {r.status_code}, query: {query}, result: {r.json()}')

    data = r.json()
    has_next = data['data']['user']['starredRepositories']['pageInfo']['hasNextPage']
    end_cursor = data['data']['user']['starredRepositories']['pageInfo']['endCursor']
    # total_count = data['data']['user']['starredRepositories']['totalCount']

    for repo in data['data']['user']['starredRepositories']['nodes']:
        name = repo['nameWithOwner']
        description = repo['description'][:200] if repo['description'] else ''
        language = repo['languages']['edges'][0]['node']['name'] if repo['languages']['edges'] else ''
        url = repo['url']
        stargazer_count = repo['stargazerCount']
        is_private = repo['isPrivate']
        items.append(Repository(name, description, language, url, stargazer_count, is_private))

    if has_next:
        query = DEFAULT_QUERY.format(username=username, after=end_cursor)
        items.extend(get_user_starred_by_username(token, username, query))
    return items
