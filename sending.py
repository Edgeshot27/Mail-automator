from email.mime.text import MIMEText
import base64

from main import authenticate


def send_mail(service,to_mail,subject,body):
    message=MIMEText(body)
    message['to']=to_mail

    message['subject']=subject
    raw=base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    service.users().messages().send(userId='me',body={'raw':raw}).execute()
    print(f'Email sent to {to_mail}')

if __name__=='__main__':
    service=authenticate()
    send_mail(service,"recipient@gmail.com","sample mail","Hello this is me aditya here")

