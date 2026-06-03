import re

pattern=r'[0-9]{10}'
text='1234567890'

res=re.fullmatch(pattern,text)
print(res.group() if res else "Not matched")

