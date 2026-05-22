def generators(res):
    for i in range(len(res)-1,-1,-1):
        yield res[i]

l=eval(input("Enter the list:"))
g=generators(l)
for i in range(len(l)):
    print(next(g),end=' ')
