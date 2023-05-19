import requests

# Set up the request parameters
url = 'https://graphql.anilist.co'
access_token = 'API KEY HERE'

# User nickname for which you want to get the ID
user_nickname = 'ch1kim0n1'

# GraphQL query to retrieve the user ID
query = '''
query ($nickname: String) {
  User (name: $nickname) {
    id
  }
}
'''

# Set up the request headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Set up the request variables
variables = {
    'nickname': user_nickname
}

# Make the request
response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    user_id = data['data']['User']['id']
    print(f"User ID for '{user_nickname}': {user_id}")
else:
    print(f"Error: {response.status_code} - {response.text}")
