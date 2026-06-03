'''
import re

pattern=r'[a-z]'
text='python version 3.13.13'

res=re.match(pattern,text)
print("Match found" if res else "Not matched")
'''








import re
pattern=r'[a-z]'
text='Python version 3.13.13'
res=re.search(pattern,text)
print(res.group() if res else "Not matched")




