import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn)) # <class 'smtplib.SMTP'>

# must call to start the connection.. 250 = means okay we connected
print(conn.ehlo()) # (250, b'smtp.gmail.com at your service, [2603:8001:7701:21d6:cc61:f19d:832f:dd06]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

# starting after ehlo encryption
conn.starttls()

# login using APP PASSWORD FROM GOOGLE
conn.login('npraglin@gmail.com','ayabgsupycmylnrq')

# send mail from - to
conn.sendmail('npraglin@gmail.com', 'pilotofdoom0@gmail.com', 'Subject: Testing Email \n\n Dear Nathan \n\n Thank you for the fish. \n\n -Nathan')