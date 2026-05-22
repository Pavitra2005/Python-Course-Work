'''
def courses():
    course='Java'
    print("In the start:",course)
    def change():
        nonlocal course
        course='python'
        print("changed:",course)
    change()

    print("Final:",course)

courses()
'''

'''
def courses():
    course='Java'
    print("In the start:",course)
    def change():
        global course
        course='python'
        print("changed:",course)
    change()

    print("Final:",course)

courses()
'''


#function names are not used as variable it looses his nature and type error can be happened.
