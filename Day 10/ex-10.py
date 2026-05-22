n=input("enter the string:")

for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("All are mutuals")
