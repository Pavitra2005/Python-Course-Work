#multiple inheritance (many parents,1-child)
class A:
    def printa(self):
        print("Parent class - A")

class B:
    def printb(self):
        print("Child class - B")

class C:
    def printc(self):
        print("Child class - C")

class D(A,B,C):
    def printd(self):
        print("Child class - D")



d=D()
d.printd()
d.printa()
d.printb()
d.printc()


