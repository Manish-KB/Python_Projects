import smtplib
import textwrap


server= smtplib.SMTP('smtp-mail.outlook.com',587)
server.starttls()
   
content='Greetings from abc clinic!!'
content=content+'''
Hello 

'''
content=content+'''
**Welcome to world's leading Clinic**
You have succesfully registered with us.

We look forward to serving you.'''
content = textwrap.dedent(content)
message = 'Subject: {}\n\n{}'.format("ABC Clinic", content)
server.login('dbms.hms.abc@outlook.com','Hello@hms123')
server.sendmail('dbms.hms.abc@outlook.com','manishkb222@gmail.com',message)
print(content)