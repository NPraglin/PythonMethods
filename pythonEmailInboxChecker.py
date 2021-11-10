import imapclient

# don't forget to import datetime!
import datetime
conn = imapclient.IMAPClient ('imap.gmail.com', ssl=True)
conn.login('npraglin@gmail.com','ayabgsupycmylnrq')
conn.select_folder('INBOX', readonly=True)

# search much be a string inside of a list/array and formatted as such, and will return emails with an ID
# if confused, reference https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
UIDs = conn.search(['SINCE', datetime.date(2021,9,10)])

#taking the ID from the returned info above, and searching for the body object
rawMessage = conn.fetch([12613], ['BODY[]', 'FLAGS'])

# pyzmail does it better once the email ID is obtained
import pyzmail

# must pass the key for the message, and the b tag of body
message = pyzmail.PyzMessage.factory(rawMessage[12613][b'BODY[]'])

# get the subject
message.get_subject()

# get the address in the... (from, to, or bcc)
message.get_addresses('from')

# return the html style and length (if exist)
message.html_part

# returns the text style and length
message.text_part

# return the text part as a string
print(message.text_part.get_payload().decode('UTF-8'))

# return folders available to select by!
conn.list_folders()

# to delete emails.. first select the folder and set readonly to false
conn.select_folder('INBOX', readonly=False)

# find the ID to delete..
UIDs = conn.search(['SINCE', datetime.date(2021,9,10)])

# delete by id.. and it worked!
conn.delete_messages([12613])