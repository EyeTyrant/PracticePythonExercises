# Exercise 5 List Overlap
# Extra 1

import random

a = []
b = []
c = []

y = random.randrange(5, 21) * 1
n = 0
while n <= y:
    a.append(random.randrange(1, 31))
    n += 1

z = random.randrange(5, 21) * 1
n = 0
while n <= z:
    b.append(random.randrange(1, 31))
    n += 1

for n in a:
    if n == n in b:
        c.append(n)
d = set(c)

print(a)
print(b)
print(d)
