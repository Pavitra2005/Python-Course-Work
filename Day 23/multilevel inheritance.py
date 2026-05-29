#multilevel inheritance
class A:
    def printa(self):
        print("Parent class - A")

class B(A):
    def printb(self):
        print("Child class - B")

class C(B):
    def printc(self):
        print("Child class - C")


c=C()
c.printa()
c.printb()
c.printc()

