#Factorial
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter the number:"))
print(factorial(n))
'''

#count the numbers
def count(n):
    c=0
    while n>0:
        n=n//10
        c+=1
    return c
print(count(241415))
        
        
    
