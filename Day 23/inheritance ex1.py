class A:
    def printa(self):
        print("Parent class - A")

class B(A):
    def printb(self):
        print("Child class - B")

a=A()
a.printa()

b=B()
b.printb()
b.printa()
