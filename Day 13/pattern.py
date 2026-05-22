'''
n=int(input("Enter the Size : "))
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()
'''


'''

n=int(input("Enter the size:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()
'''

n=int(input("Enter the size:"))
c=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+c),end=' ')
        c+=1
    print()
