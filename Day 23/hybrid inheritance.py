class A:
    def printa(self):
        print("Parent class - A")

class B:
    def printb(self):
        print("Child class - B")

class C(B,A):
    def printc(self):
        print("Child class - C")

class D(C):
    def printd(self):
        print("Child class - D")

d=D()
d.printa()
d.printb()
d.printc()
d.printd()




