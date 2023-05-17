import requests

# Set up the request parameters
url = 'https://graphql.anilist.co'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA1YWNmNDg3ZTRhY2RhYzljMWJhYzhjMDRiOTVjMzY2Yzk2NGI5YjNlZTY0NGYxZTNlMmVhMDQxNTliOTVlZTAwZWE4N2UzOTEwMGY5N2Q5In0.eyJhdWQiOiI2NDQ5IiwianRpIjoiMDVhY2Y0ODdlNGFjZGFjOWMxYmFjOGMwNGI5NWMzNjZjOTY0YjliM2VlNjQ0ZjFlM2UyZWEwNDE1OWI5NWVlMDBlYTg3ZTM5MTAwZjk3ZDkiLCJpYXQiOjE2ODQzMzk4NTQsIm5iZiI6MTY4NDMzOTg1NCwiZXhwIjoxNzE1OTYyMjU0LCJzdWIiOiI1NTYyMzQ1Iiwic2NvcGVzIjpbXX0.Y6eAjKKtsL1cTeorxoYVaiZeUGtu0Azm9k9AxIta8iH9PbCA10HfuU5CXUM2SsNIs0cQaUfHeEmoyeZ6vL8Bvsf16vimeCUGQHHmo9xeHXErhZx2J5HeVkTQI5HHOKz1DEuzlrZqiHUuAaLIh3ZOjTKkYgKNBAIW2lMzMUklgWWV_ma2A0olkkK5Maa5-s1Bt8MmYBSjirba3u2miNupQbLb76qxWnddJNHbVzoYK1otKx8U6YqxG-Re9s959uWUvXPRFfKifgUU-uePuyS0SEzam6E0kokzNpJzqKHWemTRvHXqF-G8k1oTbaqNrYN-YJhFQagWJecsLpyW1j1KJgVa-r0YKt8E_7vzwQCQEQ-Y8w-dmXGabOpHLEMR3VeAr_V2hb1vcELAa2-RwEBh3G1ZQDYP4Z5u1lPK6yot7U4waRpC89uPGb5j0KIAg-Id2WXwJwOrPV_HlbsLk2lhqQ023Hcw9Za_QaPu_e2yr2rdlNgBQfhNUI2JKfW7J3s41Pd1Pd2WXw80UCf7sSN76zi_R8H6nQvLVZBnGEAGjPrLPstEucCf2sSN76zi_xt7VHrGO3x6160Y6yDhvI'

# User ID to send the message
user_id = "5866076"

# Message content
message_content = 'Hello! This is a test message.'

# GraphQL mutation to send a message
mutation = '''
mutation CreateMessage($userId: Int!, $message: String!) {
  createMessage(userId: $userId, message: $message) {
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
    'userId': user_id,
    'message': message_content,
}

# Make the request
response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    message_id = data['data']['CreateMessage']['id']
    print(f"Message sent successfully! Message ID: {message_id}")
else:
    print(f"Error: {response.status_code} - {response.text}")
