#! python3

import re, pyperclip

# To Do: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 1234
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
((ext(\.)?\s(\d{2,5})) | (extension(\.)?\s(\d{2,5})) | (x(\.)?\s(\d{2,5})))? # extension (optional)
)
''', re.VERBOSE)

# To do: Create a regex for email addresses

emailRegex = re.compile(r'''

# something@something.com
# some.+_thing@(\d{2,5})).com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# To do: Get the text off the clipboard
text = pyperclip.paste()

# To do: Extract the email.phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
  allPhoneNumbers.append(phoneNumber[0])

# To do: Copy extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print('Copied to clipboard')