'''
import collections
s=[1,2,3,4,5,6,4,4,2,7,8,9,2,4,7,9]
print(collections.Counter(s))

d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''



'''
import collections
s='python programming'
print(collections.Counter(s))

d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)
'''


import collections
d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.popleft()
d.append(30)
d.popleft()
d.append(40)
d.append(50)
print(d)
