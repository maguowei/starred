from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

QUERY = gql("""
    query ($username: String!, $after: String) {
    user(login: $username) {
        starredRepositories(first: 100, after: $after, orderBy: {direction: DESC, field: STARRED_AT}) {
          totalCount
          nodes {
            name
            nameWithOwner
            description
            url
            stargazerCount
            forkCount
            isPrivate
            pushedAt
            updatedAt
            languages(first: 1, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                node {
                  id
                  name
                }
              }
            }
          }
          pageInfo {
            endCursor
            hasNextPage
          }
        }
      }
    }
    """
            )


class Repository:
    def __init__(self, name, description, language, url, stargazer_count, is_private):
        self.name = name
        self.description = description
        self.language = language
        self.url = url
        self.stargazer_count = stargazer_count
        self.is_private = is_private


class GitHubGQL:
    API_URL = "https://api.github.com/graphql"

    def __init__(self, token):
        self.token = token
        headers = {"Authorization": f"Bearer {token}"}
        self.transport = AIOHTTPTransport(url=self.API_URL, headers=headers)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def get_user_starred_by_username(self, username: str, after: str = ''):
        items = []
        result = self.client.execute(QUERY, variable_values={"username": username, "after": after})

        has_next = result['user']['starredRepositories']['pageInfo']['hasNextPage']
        end_cursor = result['user']['starredRepositories']['pageInfo']['endCursor']
        # total_count = result['user']['starredRepositories']['totalCount']
        for repo in result['user']['starredRepositories']['nodes']:
            name = repo['nameWithOwner']
            description = repo['description'] if repo['description'] else ''
            language = repo['languages']['edges'][0]['node']['name'] if repo['languages']['edges'] else ''
            url = repo['url']
            stargazer_count = repo['stargazerCount']
            is_private = repo['isPrivate']
            items.append(Repository(name, description, language, url, stargazer_count, is_private))

        if has_next:
            items.extend(self.get_user_starred_by_username(username, end_cursor))
        return items
