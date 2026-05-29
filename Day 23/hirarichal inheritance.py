#hierarical Inheritance(1-parent class,many child classes)
class A:
    def printa(self):
        print("Parent class - A")

class B(A):
    def printb(self):
        print("Child class - B")

class C(A):
    def printc(self):
        print("Child class - C")

class D(A):
    def printd(self):
        print("Child class - D")
class E(A):
    def printe(self):
        print("Child class - E")



b=B()
b.printb()
b.printa()

c=C()
c.printc()
c.printa()

d=D()
d.printd()
d.printa()

e=E()
e.printe()
e.printa()

