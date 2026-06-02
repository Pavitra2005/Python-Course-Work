'''
file=open('pfs53.txt','r')
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.read())
file.close()
'''


with open('pfs53.txt','r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())



try:
    with open('pfs54.txt','r') as file:
        print(file.readline())
        file.seek(0)
        print(file.readlines())
        file.seek(0)
        print(file.read())
except:
    print("File not found")
