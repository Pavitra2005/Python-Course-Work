import random
print(random.random())
print(random.randint(1,3))
print(random.uniform(1,3))

l=['python','java','c++','c','html']

print(random.choice(l))
print(random.choices(l,k=2))

print("Before:",l)
random.shuffle(l)
print("After:",l)
