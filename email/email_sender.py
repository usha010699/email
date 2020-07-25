import smtplib
from email.message import EmailMessage

email =EmailMessage()
email['from']='name'
email['to']='xxxxxxx@gmail.com'
email['subject']='you are placed'

email.set_content('i m a developer')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xxxxxxxx@gmail.com','name')
    smtp.send_message(email)
    print('all good boss!!:)')
