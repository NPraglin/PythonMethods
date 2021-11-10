import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 661-678-3391')
print ('Phone number found ' + mo.group(1) + ' ' + mo.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat|woman)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())