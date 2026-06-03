import re

pattern=r'[,-:]'
text='py,tho-n progr:am,min:g lan,gua-ge'

res=re.split(pattern,text)
print(res)
