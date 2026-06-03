import re

pattern=r'[0-9]{10}'
text='phone no: 6431555984'

res=re.sub(pattern,'**********',text)
print(res)



import re

pattern=r'[aeiouAEIOU]'
text='python programming language'

res=re.sub(pattern,'*',text)
print(res)
