'''
def reels():
    r=['1...100','101...200','201...300','301...400','401...500','501..600','601...700']
    for i in r:
        yield i

scroll = reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''


def reels():
    yield "1-10 files"
    yield "11-20 files"
    yield "21-30 files"
    yield "31-40 files"
    yield "41-50 files"
    yield "51-60 files"

scroll=reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))


    
