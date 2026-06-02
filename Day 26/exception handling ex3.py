try:
    n=-10
    if n<0:
        raise Exception("Amount needs to be > 0")
except Exception as e:
    print("Error Occurred",e)
else:
    print("No error occured")
finally:
    print("End of the program")
