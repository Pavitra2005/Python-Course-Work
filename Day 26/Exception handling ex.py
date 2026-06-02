try:
    n=10
    print(n)
    print(13+12)
    print(int(input("Enter the list:")))
    d={1:1,2:3,4:7}
    print(d[2])
    l=[34,456,134,56]
    print(l[0])
    print(1/9)
    
    if n>0:
        print("+ve")
    else:
        print("-ve")
except NameError:
    print("Define the n")
except ValueError:
    print("Give the proper datatype")
except TypeError:
    print("Give Same Datatypes")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index is not there")
except ZeroDivisionError:
    print("You can't divided with zero")

else:
    print("No error occured")
finally:
    print("End of the program")
