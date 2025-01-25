from main import authenticate
from sending import send_mail
def auto(service):
    results=service.users().messages().list(userId='me',labelIds=['UNREAD']).execute()
    messages=results.get('messages',[])

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg['payload']['headers']
        sender = next(header['value'] for header in headers if header['name'] == 'From')
        snippet = msg.get('snippet')
        print(message)
        if "hello" in snippet:
            reply=f"Hi i recieved your message :{snippet}"
            send_mail(service,sender,"reply to mail",reply)
            service.users().messages().modify(userId='me', id=message['id'],
                                              body={'removeLabelIds': ['UNREAD']}).execute()
            print(f"Reply send")


if __name__=='__main__':
    service=authenticate()
    auto(service)
