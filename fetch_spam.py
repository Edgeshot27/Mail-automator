from cProfile import label

from main import authenticate



def spam(service):
    results=service.users().messages().list(userId='me',labelIds=['SPAM']).execute()
    messages=results.get('messages',[])

    for message in messages:
            msg=service.users().messages().get(userId='me',id=message['id']).execute()
            snippet=msg['snippet']
            print(f'Snippet:{snippet}')


if __name__=='__main__':
    service=authenticate()
    spam(service)