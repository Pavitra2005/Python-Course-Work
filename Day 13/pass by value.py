'''
def display(n):
    n=n+10
    print("Inside n:",n)
n=10
display(n)
print("Outside n:",n)
'''
'''
def display(n):
    n=n+10
    print("Inside n:",n)
n=10.5
display(n)
print("Outside n:",n)
'''

'''
def display(n):
    n=n+'programming'
    print("Inside n:",n)
n='python'
display(n)
print("Outside n:",n)
'''

'''
def display(n):
    n=n+(4,5)
    print("Inside n:",n)
n=(1,2,3)
display(n)
print("Outside n:",n)
'''

'''
def display(n):
    n.append(7)
    print("Inside n:",n)
n=[1,2,3,4,5,6]
display(n)
print("Outside n:",n)
'''


'''
def display(n):
    n.add(7)
    print("Inside n:",n)
n={1,2,3,4,5,6}
display(n)
print("Outside n:",n)

'''


'''
def display():
    global n
    n+=10
    print("Inside n:",n)
n=10
display()
print("Outside n:",n)

'''


'''we use global variable there is no difference in inside and outside values.otherwise,we use immutable datatypes like int,float,bool,string,tuple had
 difference between inside and outside values '''





















