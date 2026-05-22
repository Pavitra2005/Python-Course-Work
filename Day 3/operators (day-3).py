Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=[10,20,30]
a
10
b
20
c
30
a,b,c=list(map(int,input("Enter a b c values:").split()))
Enter a b c values:2 3 4
a
2
b
3
c
4
email,password=input("Enter the Email password: ").split()
Enter the Email password: upavitra2005@gmail.com   123456
email
'upavitra2005@gmail.com'
password
'123456'
a,b=list(map(float,input("Enter a b values: ").split()))
Enter a b values: 2.4 14.5
a
2.4
b
14.5
a=2
b=5
a+b
7
a%b
2
a-b
-3
a*b
10
a/b
0.4
2**3
8
3**3
27
3***4
SyntaxError: invalid syntax
3**4
81
10/3
3.3333333333333335
a
2
b
5
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
2%5
2
a=50
a+=20
a
70
a-=20
a
50
a*=2
a
100
a/=2

a
50.0
a%=20
a
10.0
a**=2
a
100.0
b=20
a+=b
a
120.0
a=6
a%2==0 and a%3==0 and a%6==0
True
a=12
a%2==0 and a%3==0 and a%6==0
True
a=42
a%2==0 and a%3==0 and a%6==0
True
a=47
a%2==0 and a%3==0 and a%6==0
False
a%2==0 or a%3==0 or a%6==0
False
a=42
a%2==0 or a%3==0 or a%6==0
True
not a%3==0
False
not a%5==0
True
'python'
'python'
'p' in 'python'
True
'z' in 'python'
False
'i' not in 'python'
True
l=[4,5,6,7,8,9]
4 in l
True
9 in l
True
10 in l
False
9 not in l
False
t=(1,2,3,4,5)
1 in t
True
10 in t
False
2 in t
True
2 not in t
False
s={5,8,9,10,12}
2 in s
False
5 in s
True
10 not in s
False
2 not in s
True
9 in s
True
d={1:3,2:4,3:5,4:7,5:9}
d.keys()
dict_keys([1, 2, 3, 4, 5])
1 in d
True
5 in d
True
9 in d
False
10 in d
False
10 not in d
True
7 in d
False
>>> 1 not in d
False
>>> a=[1,2,3,4,5]
>>> b=[1,2,3,4,5]
>>> a==b
True
>>> a is b
False
>>> a=c
>>> c
4
>>> a==c
True
>>> c=a
>>> c
4
>>> c is a
True
>>> c is b
False
>>> id(a)
140732473377800
>>> id(b)
1677813860032
>>> id(c)
140732473377800
>>> 8&9
8
>>> 10&9
8
>>> 10 | 3
11
>>> 7^13
10
>>> 8<<1
16
>>> 8>>1
4
>>> 16<<2
64
>>> 16>>1
8
>>> ~46
-47
>>> ~49
-50
