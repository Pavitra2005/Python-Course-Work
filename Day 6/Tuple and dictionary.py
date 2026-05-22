Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
sum(l)
15
any([1.0.0.0,'',[],(),set(),{},False])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
any([1,0,0.0,'',[],(),set(),{},False])
True
all([1,0,0.0,'',[],(),set(),{},False])
False
all([1,1.1,3,'dskvkf',[1,2,3]])
True
#tuple is a collection of ordered,immutable and fixed data.It allows duplicates and heterogeneous
t=()
t=tuple()
t=(1,2,3,4,5,6)
t
(1, 2, 3, 4, 5, 6)
t.add(t)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.add(t)
AttributeError: 'tuple' object has no attribute 'add'
t.append(t)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.append(t)
AttributeError: 'tuple' object has no attribute 'append'
t=(1,1,'gnfjnvufi',[1,2,3,4],{1,2,3},(1,2,3),{1:2,3:4,2:4})
t
(1, 1, 'gnfjnvufi', [1, 2, 3, 4], {1, 2, 3}, (1, 2, 3), {1: 2, 3: 4, 2: 4})
t.append(12)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t.append(12)
AttributeError: 'tuple' object has no attribute 'append'
t(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t[3]
[1, 2, 3, 4]
t[3].append(15)
t
(1, 1, 'gnfjnvufi', [1, 2, 3, 4, 15], {1, 2, 3}, (1, 2, 3), {1: 2, 3: 4, 2: 4})
a=(1,2,4)
x,y,z=a
x
1
y
2
z
4
a=x,y,z
a
(1, 2, 4)
id(t)
2186741467360
t=t+(5,6)
t
(1, 1, 'gnfjnvufi', [1, 2, 3, 4, 15], {1, 2, 3}, (1, 2, 3), {1: 2, 3: 4, 2: 4}, 5, 6)
id(t)
2186741238016
s={'pavi','niha','pooji','deepi','chitti'}
t={'neha','vyshu','mahi'}
a=s+t
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=s+t
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s+t
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s+t
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s*3
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
t=('pavi','niha','pooji','deepi','chitti')
s=('neha','vyshu','mahi')
a=s+t
a
('neha', 'vyshu', 'mahi', 'pavi', 'niha', 'pooji', 'deepi', 'chitti')
a*3
('neha', 'vyshu', 'mahi', 'pavi', 'niha', 'pooji', 'deepi', 'chitti', 'neha', 'vyshu', 'mahi', 'pavi', 'niha', 'pooji', 'deepi', 'chitti', 'neha', 'vyshu', 'mahi', 'pavi', 'niha', 'pooji', 'deepi', 'chitti')
t[0]
'pavi'
t[5]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
a[5]
'pooji'
a[1:3:1]
('vyshu', 'mahi')
a[0:3:1]
('neha', 'vyshu', 'mahi')
a[-1:-4]
()
a[-4:-1]
('niha', 'pooji', 'deepi')
a[-1:-4:-1]
('chitti', 'deepi', 'pooji')
'pavitra' in a
False
'niha' in a
True
'mahi' in a
True
a[-1]
'chitti'
a[::-1]
('chitti', 'deepi', 'pooji', 'niha', 'pavi', 'mahi', 'vyshu', 'neha')
a[-3]
'pooji'
a.count()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)
t=(1,2,2,3,,4,5,1,2,3)
SyntaxError: invalid syntax
t=(1,2,2,3,4,5,1,2,3)
t
(1, 2, 2, 3, 4, 5, 1, 2, 3)
t.count(1)
2
t.count(2)
3
max(t)
5
min(t)
1
sorted(t)
[1, 1, 2, 2, 2, 3, 3, 4, 5]
sum(t)
23
int(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(1,2,3,4)
TypeError: int expected at most 2 arguments, got 4
int(t)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
list(t)
[1, 2, 2, 3, 4, 5, 1, 2, 3]
set(t)
{1, 2, 3, 4, 5}
bool(t)
True
dict(t)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
complex(t)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
t.inde(1)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.inde(1)
AttributeError: 'tuple' object has no attribute 'inde'. Did you mean: 'index'?
max(t)
5
data{}
SyntaxError: invalid syntax
data={}
type(data)
<class 'dict'>
data
{}
data={'userid:'101,'username':'pavi','skills':['python','java','mysql'],'gpa':'9.0'}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data={'userid':'101,'username':'pavi','skills':['python','java','mysql'],'gpa':'9.0'}
      
SyntaxError: unterminated string literal (detected at line 1)
data={'userid':101,'username':'pavi','skills':['python','java','mysql'],'gpa':9.0}
      
data
      
{'userid': 101, 'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0}
d={}
      
d[1]='int'
      
d[1.1]='float'
      
d
      
{1: 'int', 1.1: 'float'}
d[[1,2,3]='list']
      
SyntaxError: invalid syntax
d[1,2,3]='list'
      
d
      
{1: 'int', 1.1: 'float', (1, 2, 3): 'list'}
d[[1,2,3]]='list'
      
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
d[(1,2,3)]='tuple'
      
d
      
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple'}
d['False']='boolean'
      
d
      
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple', 'False': 'boolean'}
d['bfIHUHII']='string'
      
d
      
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple', 'False': 'boolean', 'bfIHUHII': 'string'}
d[1]
      
'int'
d[1.1]
      
'float'
d[(1,2,3)]
      
'tuple'
data={}
      
type(d)
      
<class 'dict'>
data=set()
      
type(data)
      
<class 'set'>
'float' in d
      
False
1 in d
      
True
'age' not in data
      
True
data
      
set()
d[1.1]
      
'float'
data['gpa']
      
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    data['gpa']
TypeError: 'set' object is not subscriptable
data
      
set()
data={'userid':101,'username':'pavi','skills':['python','java','mysql'],'gpa':9.0}
      
data
      
{'userid': 101, 'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0}
data['username']
      
'pavi'
data.get[age]
      
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    data.get[age]
NameError: name 'age' is not defined
data.get(age)
      
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    data.get(age)
NameError: name 'age' is not defined
data.get('age')
      
data.get('username')
      
'pavi'
data.get('age','age is not present)
         
SyntaxError: unterminated string literal (detected at line 1)
data.get('age','age is not present')
         
'age is not present'
data['username']='pooji'
         
data
         
{'userid': 101, 'username': 'pooji', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0}
id(data)
         
2186742052160
data['skills'].append('flask')
         
data
         
{'userid': 101, 'username': 'pooji', 'skills': ['python', 'java', 'mysql', 'flask'], 'gpa': 9.0}
id(data)
         
2186742052160

================================================================= RESTART: C:/Users/Prasa/Downloads/evenodd program.py =================================================================
45
odd
data
         
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> data={'userid':101,'username':'pavi','skills':['python','java','mysql'],'gpa':9.0}
...          
>>> data
...          
{'userid': 101, 'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0}
>>> data.update({'phoneno':'64130685789','passedoutyear':2026})
...          
>>> data
...          
{'userid': 101, 'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0, 'phoneno': '64130685789', 'passedoutyear': 2026}
>>> max(data)
...          
'username'
>>> min(data)
...          
'gpa'
>>> sorted(data)
...          
['gpa', 'passedoutyear', 'phoneno', 'skills', 'userid', 'username']
>>> data.pop()
...          
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.popitem()
...          
('passedoutyear', 2026)
>>> data
...          
{'userid': 101, 'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0, 'phoneno': '64130685789'}
>>> data.pop('userid')
...          
101
>>> data
...          
{'username': 'pavi', 'skills': ['python', 'java', 'mysql'], 'gpa': 9.0, 'phoneno': '64130685789'}
>>> data.clear()
...          
>>> data
...          
{}
