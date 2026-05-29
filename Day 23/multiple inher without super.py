class A:
    def print(self):
        print("Class-A")

class B:
    def print(self):
        print("Class-B")

class C(A,B):
    def print(self):
        A.print(self)
        B.print(self)
        print("Class-C")

c=C()
c.print()
