#!/usr/bin/python3
import smtplib
sender_mail = 'khanrakib218@gmail.com'
receivers_mail = ['shirajulislamparvez@gmail.com']
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)
try:
   password = input('Enter the password');
   smtpObj = smtplib.SMTP('gmail.com',587)
   smtpObj.login(sender_mail,password)
   smtpObj.sendmail(sender_mail, receivers_mail, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")