#!/usr/bin/env python
import smtplib
# import email modules needed
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText

# open plain text file for reading
fp = open("glist", 'rb')
msg = MIMEText(fp.read())
fp.close()

#substitute with real addresses on next two lines
me = "from@example.com"
you = "to@example.com"
msg['Subject'] = 'groceries in %s' %fp
msg['From'] = me
msg['To'] = you

#this uses gmail's secure port 587
s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
#use tls for secure login
s.starttls()
s.ehlo()
#substitute below with valid email and password
s.login('user@example.com', 'userpassword')
s.sendmail(me, [you], msg.as_string())
s.quit()
