class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,other):
        return self.num + other.num
    def __sub__(self,other):
        return self.num - other.num
    def __mul__(self,other):
        return self.num * other.num
    def __eql__(self,other):
        return self.num == other.num
    def __lt__(self,other):
        return self.num < other.num
    def __gt__(self,other):
        return self.num > other.num


a=Number(10)
b=Number(20)

print(a+b)
print(a-b)
print(a*b)
print(a==b)
print(a<b)
print(a>b)

