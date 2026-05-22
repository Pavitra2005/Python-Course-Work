Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
len(s)
6
s='HELLO'
s.lower()
'hello'
s.title()
'Hello'
s.uppercase()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
s.upper()
'HELLO'
s.lower()
'hello'
names='niharika sreeja mounika pavitra'
names
'niharika sreeja mounika pavitra'
names.split()
['niharika', 'sreeja', 'mounika', 'pavitra']
names.split('a')
['nih', 'rik', ' sreej', ' mounik', ' p', 'vitr', '']
names.split(' ',2)
['niharika', 'sreeja', 'mounika pavitra']
names.rsplit(' ',2)
['niharika sreeja', 'mounika', 'pavitra']
names
'niharika sreeja mounika pavitra'
names.split()
['niharika', 'sreeja', 'mounika', 'pavitra']
names.partition(' ')
('niharika', ' ', 'sreeja mounika pavitra')
'1.python.png'.partition('.')
('1', '.', 'python.png')
'1.python.png'.rpartition('.')
('1.python', '.', 'png')
'1.python.png'.partition(' ')
('1.python.png', '', '')
'1.python.png'.mpartition('.')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    '1.python.png'.mpartition('.')
AttributeError: 'str' object has no attribute 'mpartition'. Did you mean: 'partition'?
'1.python.png'.lpartition('.')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    '1.python.png'.lpartition('.')
AttributeError: 'str' object has no attribute 'lpartition'. Did you mean: 'partition'?
'1.python.png'.partition('.')
('1', '.', 'python.png')
l=['niharika sreeja', 'mounika', 'pavitra','srinidhi']
l
['niharika sreeja', 'mounika', 'pavitra', 'srinidhi']
''.join(l)
'niharika sreejamounikapavitrasrinidhi'
l=['niharika ,'sreeja', 'mounika', 'pavitra']
   
SyntaxError: unterminated string literal (detected at line 1)
l=['niharika' ,'sreeja', 'mounika', 'pavitra']
   
l
   
['niharika', 'sreeja', 'mounika', 'pavitra']
' '.join(l)
   
'niharika sreeja mounika pavitra'
'  '.join(l)
   
'niharika  sreeja  mounika  pavitra'
''.join(l)
   
'niharikasreejamounikapavitra'
'-'.join(l)
   
'niharika-sreeja-mounika-pavitra'
','.join(l)
   
'niharika,sreeja,mounika,pavitra'
h='            xxxxx xxxxxxxxxxx     '
   
h
   
'            xxxxx xxxxxxxxxxx     '
h.strip()
   
'xxxxx xxxxxxxxxxx'
h.lstrip()
   
'xxxxx xxxxxxxxxxx     '
h.rstrip()
   
'            xxxxx xxxxxxxxxxx'
'heello'.encode()
   
b'heello'
b'hello'.decode()
   
'hello'
text="Hello 😀"
   
text.encode()
   
b'Hello \xf0\x9f\x98\x80'
b'Hello \xf0\x9f\x98\x80'.decode()
   
'Hello 😀'
'python'.startswith('p')
   
True
'python'.endswith('on')
   
True
'python'.startswith('y')
   
False
'sfg'.isalpha()
   
True
'sow123'.isalpha()
   
False
'12413'.isalnum()
   
True
'1213dewfrw'.isalnum()
   
True
'derfnuiwvjoij'.isalnum()
...    
True
>>> l=text.encode()
...    
>>> l.decode()
...    
'Hello 😀'
>>> 'Tghvcuahcbj'.islower()
...    
False
>>> 'DEHCUJHQN'.isupper()
...    
True
>>> '    j    '.isspace()
...    
False
>>> 'xsc sdxqw dwqdqe'.istitle()
...    
False
>>> 'Dbhbui Sbhbu Ajnjkn'.istitle()
...    
True
>>> 'j'.isspace()
...    
False
>>> 'myvar'.isidentifier()
...    
True
>>> ' j '.isspace( )
...    
False
>>> '  '.isspace()
...    
True
>>> 'myvar@@'.isidentifier()
...    
False
>>> '142656'.isdecimal()
...    
True
>>> '314'.isdigit()
...    
True
>>> '23124'.isnumeric()
...    
True
