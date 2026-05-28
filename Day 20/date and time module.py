from datetime import date,time,datetime,timedelta
'''
t=date.today()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.weekday())
print(t.isoweekday())
'''

'''
dob=input("Enter the dob[YYYY-MM-DD]:")
print(dob)
'''

'''
year,month,day=list(map(int,input("Enter the dob:").split(',')))
print(date(year,month,day))
'''

'''
hours,minutes,seconds=list(map(int,input("Enter the time:").split(',')))
print(time(hours,minutes,seconds))
'''

'''
n=datetime.now()
print(n)
print(n.year)
print(n.month)
print(n.day)
print(n.hour)
print(n.minute)
print(n.second)
'''

'''
n=datetime.now()
print(n.strftime('%Y/%m/%d'))
print(n.strftime('%y/%m/%d'))
print(n.strftime('%Y/%m/%d %H:%M:%S %p'))
print(n.strftime('%a %Y/%m/%d %H:%M:%S %p'))
print(n.strftime('%a %A %Y/%m/%d %H:%M:%S %p'))
'''


n=datetime.now()
d=date.today()

a7=d-timedelta(days=20)
a15=n+timedelta(minutes=15)

print(a15)











































