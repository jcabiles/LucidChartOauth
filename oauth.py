import requests
from datetime import datetime
import os
import secrets
import codecs
import base64
from hashlib import sha1
import hmac

# static variables
consumer_key = os.environ.get('consumer_key')
client_access_key = os.environ.get('client_access_key')


def create_signature():
    # key = b"CONSUMER_SECRET&" #If you dont have a token yet
    key = f'{consumer_key}&{client_access_key}'.encode()

    # The Base String as specified here:
    raw = b"HMAC-SHA1" # as specified by OAuth

    hashed = hmac.new(key, raw, sha1)

    # The signature
    sig = hashed.digest()
    sig = base64.b64encode(sig)
    sig = sig.decode()
    #sig = sig.split('/')[1]
    return sig


# dynamic variables
timestamp = datetime.today().strftime('%s')
oauth_nonce = ''.join([secrets.choice('abcdefghijklmnopqrstuvwxyz') for i in range(11)])
oauth_signature = create_signature()

url = f'https://www.lucidchart.com/oauth/requestToken?oauth_consumer_key={consumer_key}' \
      f'&oauth_signature_method=HMAC-SHA1' \
      f'&oauth_timestamp={timestamp}' \
      f'&oauth_nonce={oauth_nonce}' \
      f'&oauth_version=1.0' \
      f'&oauth_signature={oauth_signature}'


headers = {}
payload = {}

#response = requests.request("GET", url, headers=headers, data = payload)
#access_token = response.text.encode('utf8')

print(oauth_signature)
print(url)
