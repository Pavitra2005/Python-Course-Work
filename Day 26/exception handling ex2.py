'''
try:
    n=10
    print(n)
    print(13+12)
    print(int(input("Enter the list:")))
    d={1:1,2:3,4:7}
    print(d[4])
    l=[34,456,134,56]
    print(l[0])
    print(1/9)
    
    if n>0:
        print("+ve")
    else:
        print("-ve")
except (NameError,ValueError,TypeError,KeyError,IndexError,ZeroDivisionError) as e:
    print("Error Occurred",e)
else:
    print("No error occured")
finally:
    print("End of the program")
'''



try:
    n=10
    print(n)
    print(13+12)
    print(int(input("Enter the list:")))
    d={1:1,2:3,4:7}
    print(d[4])
    l=[34,456,134,56]
    print(l[0])
    print(1/9)
    
    if n>0:
        print("+ve")
    else:
        print("-ve")
except Exception as e:
    print("Error Occurred",e)
else:
    print("No error occured")
finally:
    print("End of the program")







    
