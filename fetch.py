from main import authenticate


def fetch_all_emails(service, label_ids):

    emails = []
    results = service.users().messages().list(userId='me', labelIds=label_ids, maxResults=500).execute()
    emails.extend(results.get('messages', []))


    while 'nextPageToken' in results:
        results = service.users().messages().list(
            userId='me', labelIds=label_ids, maxResults=500, pageToken=results['nextPageToken']
        ).execute()
        emails.extend(results.get('messages', []))

        print(f"Fetched {len(emails)} emails so far...")


        if len(emails) >= 100000:
            break

    return emails[:100000]


def fetch_m(service):
    with open('emails.txt', 'w', encoding='utf-8') as file:
        messages = fetch_all_emails(service, ['INBOX'])
        print(f"Total emails fetched from Inbox: {len(messages)}")


        for message in messages[:10]:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            snippet = msg.get('snippet', 'No snippet')
            file.write(f"Message ID: {message['id']}\n")
            file.write(f"Snippet: {snippet}\n")
            file.write("=" * 50 + "\n")


if __name__ == '__main__':
    service = authenticate()
    fetch_m(service)
