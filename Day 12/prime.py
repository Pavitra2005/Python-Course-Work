
'''
#using for loop
n=int(input("Enter the number: "))
c=0
for i in range(2,n//2+1):
    if(n%i==0):
        c+=1
print("Prime Number" if c==0 else "Not prime Number")
'''

'''
def isPrime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True


n=int(input("Enter the number: "))
print("Prime Number" if isPrime(n) else "Not prime Number")
'''

#python characters

def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1

    print(f"Vol Count:{vc}")
    print(f"Con Count:{cc}")
    print(f"Dig Count:{dc}")
    print(f"Word Count:{wc}")
    print(f"Spc Count:{sc}")

check('python programming language')
     
