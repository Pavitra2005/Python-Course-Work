'''
#positional Arguments
def display(name,email,phonenumber):
    print(f"Name:{name}")
    print(f'Email:{email}')
    print(f'phone Number:{phonenumber}')

display('pavi','pavi12@gmail.com','4590293280')
display('pooji','pooji@gmail.com','4590293327')
display('4590293280','deepu','deepi23@gmail.com')
'''


'''
#keyword arguments
def display(name,email,phonenumber):
    print(f"Name:{name}")
    print(f'Email:{email}')
    print(f'phone Number:{phonenumber}')

display(name='pavi',email='pavi12@gmail.com',phonenumber='4590293280')
display(phonenumber='4590293280',name='deepu',email='deepi23@gmail.com')
'''



'''
def display(name,email,phonenumber=None,cgpa=None):
    print(f"Name:{name}")
    print(f'Email:{email}')
    print(f'phone Number:{phonenumber}')
    print(f"CGPA:{cgpa}")
    

display('pavi','pavi12@gmail.com','4590293280')
display('4590293280','deepu','deepi23@gmail.com',8.2)
display('pavitra','pavitra1256@gmail.com',9.1)
'''


'''
def display(*names):
    print(names)

display('pavi')
display('pooji','deepi')
display('mahi','hemu','anji')
display('subbu','seetha','ram','vyshu')
'''


def display(**names):
    print(names)

display(n1='pavi')
display(n2='pooji',n3='deepi')
display(n4='mahi',n5='hemu',n6='anji')
display(n7='subbu',n8='seetha',n9='ram',n10='vyshu')

































































