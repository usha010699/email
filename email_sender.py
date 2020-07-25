import smtplib
from email.message import EmailMessage

email =EmailMessage()
email['from']='email name'
email['to']='xxxxxxxx@gmail.com'
email['subject']='you are placed'

email.set_content('i m a developer')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ur email id@gmail.com','ur email id pass')
    smtp.send_message(email)
    print('all good boss!!:)')
