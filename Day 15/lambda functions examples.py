'''
add=lambda a,b:a+b
print(add(3,4))
'''


'''
add=lambda base,power:base**power
print(add(2,3))
'''


'''
wish=lambda name:f'{name},welcome to the python'
print(wish('pavitra'))
'''

'''
check=lambda num:'Even' if num%2==0 else 'odd'
print(check(18))
print(check(5))
'''

'''
square=lambda num:num**2
print(square(3))
'''

'''
check=lambda a,b:max(a,b)
print(check(3,4))
print(check(67,57))
'''

'''
check=lambda s:len(s)
print(check('python'))
print(check('python programming'))
'''

'''
check=lambda s:'starts with vowel' if s[0] in 'aeiouAEIOU' else 'not starts with vowel'
s=input("Enter the name:")
print(check(s))
'''

'''
check=lambda email:email.split('@')[-1]
print(check('upavitra2005@gmail.com'))
print(check('pavitra@infosys.com'))
'''

'''
#check leap year or not
check=lambda year:"Leap Year" if year%400==0 or (year%4==0 and year%100!=0) else "not a Leap Year"
print(check(2024))
print(check(2026))
'''

'''
#unit digit
check=lambda year:year%10
print(check(2024))
print(check(2026))
'''

'''
#square of items in list
l=["hello","hi","world","python"]
res=list(map(lambda i:i.upper(),l))
print(res)
'''

'''
l=[1,2,3,4,5]
res=list(map(lambda i:i+10,l))
print(res)
'''


'''
l={'sahil':45,'niharika':80,'mounika':65,'charan':92}
res=dict(sorted(l.items()))
print(res)
'''

'''
l={'sahil':45,'niharika':80,'mounika':65,'charan':92}
print(dict(sorted(l.items(),key=lambda i:i[1])))
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))
'''

'''
l=[1,2,2,3,4,5,5,6,12,13,55,64,68,96,108]
res=list(filter(lambda i:i%2!=0,l))
print(res)
'''

'''
l='python programming'
res=list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)
'''

'''
#vowels
l=['operator','oops','control','conditional','files','exceptional']
res=list(filter(lambda i:i[0] in 'aeiouAEIOU',l))
print(res)
'''

'''
#consonents
l=['operator','oops','control','conditional','files','exceptional']
res=list(filter(lambda i:i[0]  not in 'aeiouAEIOU',l))
print(res)
'''

'''
data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res=list(filter(lambda i:data[i]['stock']==0,data))
print(res)
'''

'''
data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res=list(filter(lambda i:data[i]['stock']!=0,data))
print(res)
'''

'''
data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)

'''

'''
data={
    'dell':{'stock':0,'price':89000},
    'lenovo':{'stock':15,'price':55000},
    'mac':{'stock':8,'price':120000},
    'hp':{'stock':12,'price':45000},
    'thinkpad':{'stock':0,'price':37000}
    }
res={i:data[i]['price'] for i in data}

l2h=dict(sorted(res.items(),key=lambda i:i[1]))
h2l=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))

print("Low to high:")
print(l2h)

print("High to low")
print(h2l)
'''


from functools import reduce
l=[1,2,2,3,4,5,5,6,12,23,34567,254,45679]
m=['operator','oops','control','conditional','files','exceptional']
ms=reduce(lambda sum,i:sum+','+i,m)
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p,ms)
















































































