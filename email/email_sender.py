import smtplib
from email.message import EmailMessage

email =EmailMessage()
email['from']='sha natashah'
email['to']='nishakannan1705@gmail.com'
email['subject']='you are placed'

email.set_content('i m a developer')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ushanatashah@gmail.com','usha kannan')
    smtp.send_message(email)
    print('all good boss!!:)')