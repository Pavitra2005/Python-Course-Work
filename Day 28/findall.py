
import re

pattern=r'[a-z]{3}'
text='python version 3.13.13'

res=re.findall(pattern,text)
print(res)




