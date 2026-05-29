class A:
    def print(self):
        print("Class-A")

class B(A):
    def print(self):
        super().print()
        print("Class-B")

b=B()
b.print()
