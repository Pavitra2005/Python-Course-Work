
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)


'''
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)
'''

'''
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s='python'
display(s,0)
'''

'''
def display(s,ind,end):
    if ind==len(s)+1:
        return
    print(s[ind:end])
    display(s,ind+1,end+1)
s='python programming'
display(s,0,4)
'''
'''
def display(s):
    i=1
    s=0
    s+=i
    return
print(s)
s=10
display(s)
'''
