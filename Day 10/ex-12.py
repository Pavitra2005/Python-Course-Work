a,b,c=map(int,input().split())
if(a==b and b==c):
    print("equilateral")
elif(a==b or b==c or c==a):
    print("Isosceles")
else:
    print("Scalene")
