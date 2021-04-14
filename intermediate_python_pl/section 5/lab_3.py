import smtplib

mailFrom = 'Your python mailing'
mailTo = ['mjanusz1109+python@gmail.com', 'janusz.j.michal@gmail.com']
mailSubject = 'python mail'
mailBody = '''Hello

This mail confirms that it is possible to send mails using python

Have a nice day!'''

message = f'''From: {mailFrom}
Subject: {mailSubject}

{mailBody}
'''

user = 'mjanusz1109@gmail.com'
password = 'Nordea@66'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('an error occured')
