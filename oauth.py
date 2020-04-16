# Using OAuth1Session
from requests_oauthlib import OAuth1Session

# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1
import argparse
from urllib.parse import parse_qs

# define LucidChart URLs
request_token_url = 'https://www.lucidchart.com/oauth/requestToken'
authorization_url = 'https://www.lucidchart.com/oauth/authorize'
access_token_url = 'https://www.lucidchart.com/oauth/accessToken'

# grab client credentials from local machine's configuration scripts (e.g., bash_profile)
client_key = os.environ.get('oauth_consumer_key')
client_secret = os.environ.get('client_secret')

# Get resource tokens
oauth = OAuth1(client_key, client_secret=client_secret)
r = requests.post(url=request_token_url, auth=oauth)
credentials = parse_qs(r.content.decode())
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]

lucid_oauth = OAuth1Session(client_key,
                            client_secret=client_secret,
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')

# test outputs
print(client_key)
print(client_secret)
print(resource_owner_key)
print(resource_owner_secret)
