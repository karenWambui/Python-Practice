import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string ='Andrei'
pattern2= re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password ='hdjkahskdha5534%$9'
#string = 'super87sectre%$#7'
a = pattern.search(string) 
check = pattern2.fullmatch(password)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
print(check)
