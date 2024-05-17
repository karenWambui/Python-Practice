import re



pattern = re.compile('this')
string = 'search inside of this text please!'

a = re.search('this',string)
print(a.start())