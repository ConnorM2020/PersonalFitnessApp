import numpy as np
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

df = pd.DataFrame({'a' : [1, 2, 3]})
df.to_csv('C:\\Users\\A2N\\Desktop\\Python_Scheduler\\data_mail_new.csv', index = False)

msg = MIMEMultipart()
msg['From'] = 'first.last@outlook.com'
msg['To'] = 'first.last@gmail.com'
msg['Subject'] = 'Robot Mail'
body = 'Hello buddy, long time no see.'
msg.attach(MIMEText(body, 'plain'))
attachment=open('C:\\Users\\A2N\\Desktop\\Python_Scheduler\\data_mail_new.csv','rb').read()
x = MIMEBase('application', 'octet-stream')
x.set_payload(attachment)
encoders.encode_base64(x)
x.add_header('Content-Disposition', 'attachment', filename='data_mail_new.csv')
msg.attach(x)

# The port_number and server address below should be changed to your SMTP server details, 
# and the login credentials should be changed as well
port_number = 1025
mailserver = smtplib.SMTP('localhost',port_number)
mailserver.login("first.last@outlook.com", "PASSWORD1234")
mailserver.sendmail('first.last@outlook.com','first.last@gmail.com',msg.as_string())
mailserver.quit()  