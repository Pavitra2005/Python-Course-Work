Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
l=['fghi',1,12.3,[1,2],(1,2),True,{1:1},{1,2,3},None]
l
['fghi', 1, 12.3, [1, 2], (1, 2), True, {1: 1}, {1, 2, 3}, None]
#list is heterogenous
#concatenation
a=[1,2,3,4]
b=[2,4,7,9]
a+b
[1, 2, 3, 4, 2, 4, 7, 9]
a*10
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=['niharika','pavitra','sreeja','mounika','srinidhi']
l[0]
'niharika'
l[1]
'pavitra'
l[-1]
'srinidhi'
l[-4]
'pavitra'
l[:3]
['niharika', 'pavitra', 'sreeja']
l[3:]
['mounika', 'srinidhi']
l[::-1]
['srinidhi', 'mounika', 'sreeja', 'pavitra', 'niharika']
l
['niharika', 'pavitra', 'sreeja', 'mounika', 'srinidhi']
l[-4:-3]
['pavitra']
>>> l[-3:-2]
['sreeja']
>>> l[-4:-2]
['pavitra', 'sreeja']
>>> l[-4:-6]
[]
>>> l[-4:-5]
[]
>>> l[-5:-3]
['niharika', 'pavitra']
>>> l[-1]
'srinidhi'
>>> 'pavitra' in l
True
>>> 'niha' in l
False
>>> 'pooji' not in l
True
>>> l=[]
>>> l=list()
>>> l=['niharika','pavitra','sreeja','mounika','srinidhi']
>>> id(l)
1503819051008
>>> l[0]
'niharika'
>>> l[0]='geethanjali'
>>> l
['geethanjali', 'pavitra', 'sreeja', 'mounika', 'srinidhi']
>>> l[3]
'mounika'
>>> l[3]='pooji'
>>> l
['geethanjali', 'pavitra', 'sreeja', 'pooji', 'srinidhi']
>>> id(l)
1503819051008
>>> l.add('niharika')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l.add('niharika')
AttributeError: 'list' object has no attribute 'add'
>>> a=['niharika']
>>> l+a
['geethanjali', 'pavitra', 'sreeja', 'pooji', 'srinidhi', 'niharika']
>>> l.append('sravani')
>>> l
['geethanjali', 'pavitra', 'sreeja', 'pooji', 'srinidhi', 'sravani']
