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

def send_message(anilist_id, message):
    api_url = "https://graphql.anilist.co"

    query = """
    mutation ($id: Int, $message: String) {
        SaveMessage(userId: $id, message: $message) {
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
        "Authorization": "Bearer emNkFkhbcJ890tFfcZjWqknzFVPno7jFSHr8pHZO"  # API key here
    }

    response = requests.post(api_url, json={"query": query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        result = response.json()
        saved_message = result["data"]["SaveMessage"]
        print(f"Message sent to user {saved_message['id']}: {saved_message['message']}")
    else:
        print("Failed to send message.")

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
