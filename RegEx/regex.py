import re

# findall()
# search()
# split()
# sub()
# finditer()

text = """Name: John Doe
Address: 123 Main Street, Ureeee Cityville, State, 12345
Mobile: +919123456710
Email: john.rdoe@example.com
Fax: (555) 987-6543"""

# all matches
# p = re.compile(r'.')
# data = p.finditer(text)
# for info in data:
#     print(info)

# p = re.compile(r'.4')
# p = re.compile(r'^Name')  # ^ -> use for starting
# p = re.compile(r'543$') # $ -> use for endswith
p = re.compile(r're*') # this give pattern with minimum zero 'e'
p = re.compile(r're+') # this give pattern with minimum one 'e'
p = re.compile(r're{3}') # it show the count of 'e'
p = re.compile(r'(re)') # () it work as group
p = re.compile(r'(re)|(ee)')
p = re.compile(r'(Str) | M')

p = re.compile(r'\AName')
p = re.compile(r'\bAddress')
p = re.compile(r'\bFax')
p = re.compile(r'543\b')
p = re.compile(r'567\b')

p = re.compile(r'\d{3}-\d{4}')

# find mobile number
p = re.compile(r'\+91\d{10}')
data = p.finditer(text)

for info in data:
    print(info)

data = p.findall()

# print('\n')
# print(r'\n')

# p = re.compile(r'123')

# data = p.finditer(text)

# for info in data:
#     print(info)
    
# print(text[25:28])
# print(text[60:63])
# print(text[80:83])

