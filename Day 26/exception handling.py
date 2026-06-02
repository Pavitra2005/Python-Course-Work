try:
    n=10
    if n>0:
        print("+ve")
    else:
        print("-ve")
except NameError:
    print("Define the n")
else:
    print("No error occured")
finally:
    print("End of the program")
