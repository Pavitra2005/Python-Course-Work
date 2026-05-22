def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
def generators(res):
    for i in res:
        yield i

r=factors(38)
g=generators(r)
for i in range(len(r)):
    print(next(g))
