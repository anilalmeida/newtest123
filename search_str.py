import re

string = 'search this inside of this text please'

pattern = re.compile('search this')

a = re.search('this', string)
print(re.search('this', string))
print(a.span())
print(a.start())
print(a.group())

b = pattern.search(string)
print(f'14 {b}')
c = pattern.findall((string))
print(c)
d = pattern.match(string)
print(f'18 {d} {d.span()}')
