'''
with open('pfs53.txt','w') as file:
    file.write('pinky')
    file.write('\nchitti')
    file.write('\nsmiley')
    file.seek(0)
    print(file.read())
'''

'''
#W+ is used to read and write
with open('pfs53.txt','w+') as file:
    file.write('pinky')
    file.write('\nchitti')
    file.write('\nsmiley')
    file.seek(0)
    print(file.read())
'''

'''
#a+ is used to append and read
with open('pfs53.txt','a+') as file:
    file.write('pinky')
    file.write('\nchitti')
    file.write('\nsmiley')
    file.seek(0)
    print(file.read())
'''
