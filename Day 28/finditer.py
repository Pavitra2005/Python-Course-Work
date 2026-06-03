import re

pattern=r'[0-9]{2}'
text='python version 3.13.13'

res=re.finditer(pattern,text)

for i in res:
    print(i.group(),i.start())



