import requests

DEFAULT_QUERY = """
{{
  user(login: "{username}") {{
    starredRepositories(first: 100, after: "{after}"){{
      totalCount
      nodes {{
        name
        description
        stargazerCount
        url
        forkCount
        languages(first: 1, orderBy: {{field: SIZE, direction: DESC}}) {{
          edges {{
            node {{
              id
              name
            }}
          }}
        }}
        nameWithOwner
        pushedAt
        releases(orderBy: {{field: CREATED_AT, direction: ASC}}, last: 1) {{
          edges {{
            node {{
              name
              tagName
              createdAt
              updatedAt
              url
            }}
          }}
        }}
        updatedAt
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
    def __init__(self, name, description, language, url, stargazer_count):
        self.name = name
        self.description = description
        self.language = language
        self.url = url
        self.stargazer_count = stargazer_count


def get_user_starred_by_username(token, username, query=None):
    items = []
    headers = {"Authorization": f"Bearer {token}"}
    if query is None:
        query = DEFAULT_QUERY.format(username=username, after='')
    r = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    data = r.json()
    has_next = data['data']['user']['starredRepositories']['pageInfo']['hasNextPage']
    end_cursor = data['data']['user']['starredRepositories']['pageInfo']['endCursor']
    # total_count = data['data']['user']['starredRepositories']['totalCount']

    for repo in data['data']['user']['starredRepositories']['nodes']:
        name = repo['nameWithOwner']
        description = repo['description']
        language = repo['languages']['edges'][0]['node']['name'] if repo['languages']['edges'] else ''
        url = repo['url']
        stargazer_count = repo['stargazerCount']
        items.append(Repository(name, description, language, url, stargazer_count))

    if has_next:
        query = DEFAULT_QUERY.format(username=username, after=end_cursor)
        items.extend(get_user_starred_by_username(token, username, query))
    return items