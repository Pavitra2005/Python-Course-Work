Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
a=10.3
int(a)
10
str(a)
'10.3'
complex(a)
(10.3+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
bool(a)
True
c=2+3j
c
(2+3j)
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c
     )
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c
TypeError: 'complex' object is not iterable
tuple(c)
         
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
         
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
         
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
         
True
s='python'
         
s
         
'python'
int(s)
         
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
float(s)
         
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
complex(a)
         
(10.3+0j)
complex(s)
         
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
         
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
         
('p', 'y', 't', 'h', 'o', 'n')
set(s)
         
{'h', 'p', 't', 'y', 'o', 'n'}
dict(s)
         
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
         
True
s='10'
         
int(s)
         
10
float(s)
         
10.0
complex(s)
         
(10+0j)
list(s)
         
['1', '0']
tuple(s)
         
('1', '0')
set(s)
         
{'0', '1'}
dict(s)
         
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
         
True
l=[2,4,5]
         
l
         
[2, 4, 5]
int(l)
         
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
         
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
         
'[2, 4, 5]'
complex(l)
         
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(l)
         
(2, 4, 5)
set(l)
         
{2, 4, 5}
dict(l)
         
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
         
True
t=(1,2,3,4,5)
...          
>>> int(t)
...          
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(t)
...          
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(t)
...          
'(1, 2, 3, 4, 5)'
>>> complex(t)
...          
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> list(t)
...          
[1, 2, 3, 4, 5]
>>> set(t)
...          
{1, 2, 3, 4, 5}
>>> dict(t)
...          
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
...          
True
>>> s={1,2,3,4}
...          
>>> int(s)
...          
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
...          
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
         
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
str(s)
         
'{1, 2, 3, 4}'
list(s)
         
[1, 2, 3, 4]
tuple(s)
         
(1, 2, 3, 4)
dict(s)
         
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
         
True
d={1:1,2:2,3:3}
         
int(d)
         
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
         
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(s)
         
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
complex(d)
         
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(d)
         
[1, 2, 3]
tuple(d)
         
(1, 2, 3)
str(d)
         
'{1: 1, 2: 2, 3: 3}'
set(d)
         
{1, 2, 3}
bool(s)
         
True
b=True
         
int(b)
         
1
float(b)
         
1.0
complex(b)
         
(1+0j)
str(b)
         
'True'
list(b)
         
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
         
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
         
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(b)
         
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
bool(b)
         
True
a=10
         
b=10.2
         
c='python'
         
print(a,b,c)
         
10 10.2 python
print('a=',a,'b=',b,'c=',c)
         
a= 10 b= 10.2 c= python
print('a=',a,'b=',b,'c=',c,sep='')
         
a=10b=10.2c=python
print('a=',a,'b=',b,'c=',c,sep='\n')
         
a=
10
b=
10.2
c=
python
print('a=',a,'b=',b,'c=',c,sep='\t')
         
a=	10	b=	10.2	c=	python
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
         
a=	10	b=	10.2	c=	python

print('a=',a,'b=',b,'c=',c,sep='\t',end='@@@')
         
a=	10	b=	10.2	c=	python@@@
print(f'a:{a},b:{b},c={c}')
         
a:10,b:10.2,c=python
print(f'a:{a} b:{b} c={c}')
         
a:10 b:10.2 c=python
print('a=%d b=%f c=%s')
         
a=%d b=%f c=%s
print('a=%d b=%f c=%s'%(a,b,c))
         
a=10 b=10.200000 c=python
print('a={} b={} c={}',format(a,b,c))
         
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print('a={} b={} c={}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
print('a={} b={} c={}'.format(a,b,c))
         
a=10 b=10.2 c=python
print('a={2} b={0} c={1}',format(a,b,c))
         
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    print('a={2} b={0} c={1}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
print('a={2} b={0} c={1}'.format(a,b,c))
         
a=python b=10 c=10.2
a=input()
         
pavi
a
         
'pavi'
name=input("ENter your name:")
         
ENter your name:Pavitra
name
         
'Pavitra'
type(name)
         
<class 'str'>
age=input("Enter the age")
         
Enter the age21
age
         
'21'
type(age)
         
<class 'str'>
age=int(input("Enter your age"))
         
Enter your age21
age
         
21
type(age)
         
<class 'int'>
gpa=float(input("Enter your CGPA"))
         
Enter your CGPA9.0
gpa
         
9.0
type(gpa)
         
<class 'float'>
'niharika sreeja pavitra mounika sravani'.split()
         
['niharika', 'sreeja', 'pavitra', 'mounika', 'sravani']
names=input("Enter the names:").split()
         
Enter the names:niharika sreeja pavitra mounika sravani
names
         
['niharika', 'sreeja', 'pavitra', 'mounika', 'sravani']
age=input("Enter the ages:").split()
         
Enter the ages:21 22 21 23 22
age
         
['21', '22', '21', '23', '22']
map(int,input("Enter the ages:").split())
         
Enter the ages:21 22 21 23 22
<map object at 0x000002587194FA30>
age=list(map(int,input("Enter the ages:").split())
)
         
Enter the ages:21 22 21 23 22
age
         
[21, 22, 21, 23, 22]
age=list(map(float,input("Enter the ages:").split())
)
         
Enter the ages:44.5 67.8 76.5 335.4 432.3
age
         
[44.5, 67.8, 76.5, 335.4, 432.3]
names=tuple(input("ENter the names"))
         
ENter the names p v n a q
names
         
(' ', 'p', ' ', 'v', ' ', 'n', ' ', 'a', ' ', 'q')
names=tuple(input("ENter the ages").split())
         
ENter the ages1 2 4
names
         
('1', '2', '4')
age=tuple(map(float,input("Enter the ages:").split())
)
         
Enter the ages:21 22 2 3 4
age
         
(21.0, 22.0, 2.0, 3.0, 4.0)
age=tuple(map(int,input("Enter the ages:").split())
)
         
Enter the ages:2 3 4 5 6
age
         
(2, 3, 4, 5, 6)
