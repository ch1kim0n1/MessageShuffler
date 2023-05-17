import requests
import json
import random

def get_ids_and_messages(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    ids_and_messages = []
    for id, message in data.items():
        ids_and_messages.append((id, message))

    return ids_and_messages

# ---------------------------------------------TEMPLATE USED----------------------------------------------------

def send_message(anilist_id, message):
    api_url = "https://graphql.anilist.co"

    query = """
    mutation ($id: Int, $message: String) {
        SaveMessage(receiptId: $id, message: $message) {
            id
            message
        }
    }
    """

    variables = {
        "id": anilist_id,
        "message": message
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA1YWNmNDg3ZTRhY2RhYzljMWJhYzhjMDRiOTVjMzY2Yzk2NGI5YjNlZTY0NGYxZTNlMmVhMDQxNTliOTVlZTAwZWE4N2UzOTEwMGY5N2Q5In0.eyJhdWQiOiI2NDQ5IiwianRpIjoiMDVhY2Y0ODdlNGFjZGFjOWMxYmFjOGMwNGI5NWMzNjZjOTY0YjliM2VlNjQ0ZjFlM2UyZWEwNDE1OWI5NWVlMDBlYTg3ZTM5MTAwZjk3ZDkiLCJpYXQiOjE2ODQzMzk4NTQsIm5iZiI6MTY4NDMzOTg1NCwiZXhwIjoxNzE1OTYyMjU0LCJzdWIiOiI1NTYyMzQ1Iiwic2NvcGVzIjpbXX0.Y6eAjKKtsL1cTeorxoYVaiZeUGtu0Azm9k9AxIta8iH9PbCA10HfuU5CXUM2SsNIs0cQaUfHeEmoyeZ6vL8Bvsf16vimeCUGQHHmo9xeHXErhZx2J5HeVkTQI5HHOKz1DEuzlrZqiHUuAaLIh3ZOjTKkYgKNBAIW2lMzMUklgWWV_ma2A0olkkK5Maa5-s1Bt8MmYBSjirba3u2miNupQbLb76qxWnddJNHbVzoYK1otKx8U6YqxG-Re9s959uWUvXPRFfKifgUU-uePuyS0SEzam6E0kokzNpJzqKHWemTRvHXqF-G8k1oTbaqNrYN-YJhFQagWJecsLpyW1j1KJgVa-r0YKt8E_7vzwQCQEQ-Y8w-dmXGabOpHLEMR3VeAr_V2hb1vcELAa2-RwEBh3G1ZQDYP4Z5u1lPK6yot7U4waRpC89uPGb5j0KIAg-Id2WXwJwOrPV_HlbsLk2lhqQ023Hcw9Za_QaPu_e2yr2rdlNgBQfhNUI2JKfW7J3s41v1Pd1c7zma8m9RQXNrISydEt8LhvSSwZg4xK05XR_h8y3z_ZSYc24q4ReNg_R8H6nQvLVZBnGEAGjPrLPstEucCf2sSN76zi_qFSjHzgjA6uCsmS-o_H7WECkqdlQt53cCXiaImxy6_xt7VHrGO3xVw80UCf71X6160Y6yDhvI"  # API key here
    }

    response = requests.post(api_url, json={"query": query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        result = response.json()
        saved_message = result["data"]["SaveMessageActivity"]
        print(f"Message sent to user {saved_message['id']}: {saved_message['message']}")
    else:
        print("Failed to send message.")
        
#--------------------------------------------------------------------------------------------------------------------

def send_random_message(ids_and_messages, messages_sent):
    remaining_messages = [message for id, message in ids_and_messages if message not in messages_sent]
    if not remaining_messages:
        return None  # Return None if all messages have been sent
    message = random.choice(remaining_messages)
    messages_sent.add(message)
    return message

def check_for_repeats(messages):
    messages_seen = set()
    for message in messages:
        if message in messages_seen:
            return True
        messages_seen.add(message)
    return False

def main():
    filename = "data.json"
    ids_and_messages = get_ids_and_messages(filename)

    original_ids_and_messages = []
    new_ids_and_messages = []

    messages_sent = set()  # Initialize an empty set to store sent messages

    for id, message in ids_and_messages:
        original_ids_and_messages.append((id, "Original", message))
        random_message = send_random_message(ids_and_messages, messages_sent)
        if random_message is None:
            print("Not enough unique messages available.")
            return
        new_ids_and_messages.append((id, "New", random_message))
        send_message(id, random_message)

    print("Original IDs and Messages:")
    for id, type, message in original_ids_and_messages:
        print(f"{id} - {type} - {message}")

    print("New IDs and Messages:")
    for id, type, message in new_ids_and_messages:
        print(f"{id} - {type} - {message}")

if __name__ == "__main__":
    main()