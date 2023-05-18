#'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA1YWNmNDg3ZTRhY2RhYzljMWJhYzhjMDRiOTVjMzY2Yzk2NGI5YjNlZTY0NGYxZTNlMmVhMDQxNTliOTVlZTAwZWE4N2UzOTEwMGY5N2Q5In0.eyJhdWQiOiI2NDQ5IiwianRpIjoiMDVhY2Y0ODdlNGFjZGFjOWMxYmFjOGMwNGI5NWMzNjZjOTY0YjliM2VlNjQ0ZjFlM2UyZWEwNDE1OWI5NWVlMDBlYTg3ZTM5MTAwZjk3ZDkiLCJpYXQiOjE2ODQzMzk4NTQsIm5iZiI6MTY4NDMzOTg1NCwiZXhwIjoxNzE1OTYyMjU0LCJzdWIiOiI1NTYyMzQ1Iiwic2NvcGVzIjpbXX0.Y6eAjKKtsL1cTeorxoYVaiZeUGtu0Azm9k9AxIta8iH9PbCA10HfuU5CXUM2SsNIs0cQaUfHeEmoyeZ6vL8Bvsf16vimeCUGQHHmo9xeHXErhZx2J5HeVkTQI5HHOKz1DEuzlrZqiHUuAaLIh3ZOjTKkYgKNBAIW2lMzMUklgWWV_ma2A0olkkK5Maa5-s1Bt8MmYBSjirba3u2miNupQbLb76qxWnddJNHbVzoYK1otKx8U6YqxG-Re9s959uWUvXPRFfKifgUU-uePuyS0SEzam6E0kokzNpJzqKHWemTRvHXqF-G8k1oTbaqNrYN-YJhFQagWJecsLpyW1j1KJgVa-r0YKt8E_7vzwQCQEQ-Y8w-dmXGabOpHLEMR3VeAr_V2hb1vcELAa2-RwEBh3G1ZQDYP4Z5u1lPK6yot7U4waRpC89uPGb5j0KIAg-Id2WXwJwOrPV_HlbsLk2lhqQ023Hcw9Za_QaPu_e2yr2rdlNgBQfhNUI2JKfW7J3s41Pd1Pd2WXw80UCf7sSN76zi_R8H6nQvLVZBnGEAGjPrLPstEucCf2sSN76zi_xt7VHrGO3x6160Y6yDhvI'


import requests
import json

# Set your access token and recipient user ID
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA1YWNmNDg3ZTRhY2RhYzljMWJhYzhjMDRiOTVjMzY2Yzk2NGI5YjNlZTY0NGYxZTNlMmVhMDQxNTliOTVlZTAwZWE4N2UzOTEwMGY5N2Q5In0.eyJhdWQiOiI2NDQ5IiwianRpIjoiMDVhY2Y0ODdlNGFjZGFjOWMxYmFjOGMwNGI5NWMzNjZjOTY0YjliM2VlNjQ0ZjFlM2UyZWEwNDE1OWI5NWVlMDBlYTg3ZTM5MTAwZjk3ZDkiLCJpYXQiOjE2ODQzMzk4NTQsIm5iZiI6MTY4NDMzOTg1NCwiZXhwIjoxNzE1OTYyMjU0LCJzdWIiOiI1NTYyMzQ1Iiwic2NvcGVzIjpbXX0.Y6eAjKKtsL1cTeorxoYVaiZeUGtu0Azm9k9AxIta8iH9PbCA10HfuU5CXUM2SsNIs0cQaUfHeEmoyeZ6vL8Bvsf16vimeCUGQHHmo9xeHXErhZx2J5HeVkTQI5HHOKz1DEuzlrZqiHUuAaLIh3ZOjTKkYgKNBAIW2lMzMUklgWWV_ma2A0olkkK5Maa5-s1Bt8MmYBSjirba3u2miNupQbLb76qxWnddJNHbVzoYK1otKx8U6YqxG-Re9s959uWUvXPRFfKifgUU-uePuyS0SEzam6E0kokzNpJzqKHWemTRvHXqF-G8k1oTbaqNrYN-YJhFQagWJecsLpyW1j1KJgVa-r0YKt8E_7vzwQCQEQ-Y8w-dmXGabOpHLEMR3VeAr_V2hb1vcELAa2-RwEBh3G1ZQDYP4Z5u1lPK6yot7U4waRpC89uPGb5j0KIAg-Id2WXwJwOrPV_HlbsLk2lhqQ023Hcw9Za_QaPu_e2yr2rdlNgBQfhNUI2JKfW7J3s41v1Pd1c7zma8m9RQXNrISydEt8LhvSSwZg4xK05XR_h8y3z_ZSYc24q4ReNg_R8H6nQvLVZBnGEAGjPrLPstEucCf2sSN76zi_qFSjHzgjA6uCsmS-o_H7WECkqdlQt53cCXiaImxy6_xt7VHrGO3xVw80UCf71X6160Y6yDhvI'
recipient_user_id = "5866076"

# GraphQL API endpoint
url = 'https://graphql.anilist.co'

# GraphQL mutation payload
mutation = '''
mutation($userId: Int, $message: String) {
  SaveMessageActivity(recipientId: $userId, message: $message) {
    id
  }
}
'''

# Define the variables for the mutation
variables = {
    'userId': recipient_user_id,
    'message': 'Hello, this is a test message!'
}

# Prepare the headers for the API request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Make the API request
response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)

# Check the response status code
if response.status_code != 200:
    data = response.json()
    if 'errors' in data:
        # Error occurred
        print('Error:', data['errors'][0]['message'])
else:
    # Message sent successfully
    data = response.json()
    message_id = data['data']['SaveMessageActivity']['id']
    print(f'Message sent successfully! Message ID:')
