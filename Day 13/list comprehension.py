'''
l=[1,2,3,4,5,56,6,7]
res=[i+10 for i in l]
print(res)
'''
'''
l=[1,2,3,4,5,56,6,7]
res=[i*l[i] for i in range(len(l))]
print(res)
'''

'''
l=[1,2,3,4,5,56,6,7]
res=[i**3 for i in l]
print(res)
'''

l=[1,2,3,4,5,56,6,7]
res=[i if i%2==0 else 0 for i in l]
print(res)
