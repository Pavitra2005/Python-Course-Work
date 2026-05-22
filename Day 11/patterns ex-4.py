'''
n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
'''

'''
n=int(input("enter the number:"))
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

'''

'''
n=int(input("Enter the size:"))
for i in range(n):
    for spc in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
'''

'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print(int(j%2==0),end=' ')
    print()

'''

'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print(int(j%2!=0),end=' ')
    print()

'''

'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print(int((i+j)%2==0),end=' ')
    print()
'''



'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
     if(i==0 or i==(n-1)):
        print('*',end=' ')
     elif(j==0 or j==(n-1)):
         print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
'''    

'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
     if(i==0 or i==(n-1) or i==(n-3)):
        print('*',end=' ')
     elif(j==0 or j==(n-1) or j==(n-3)):
         print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
'''



'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
     if(i==0 or i==(n-1) or (i+j)==(n-1)):
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
'''


'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
     if((i+j)==(n-1) or i==j):
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
'''



n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
     if(i==0 or j==0 or (i==(n-1) and j<=n//2) or (j==n//2 and i>=n//2) or (j==(n-1) and i==n//2)):
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()














































