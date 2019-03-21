# Exercise 5 List Overlap
# Extra 2

import random

a = random.sample(range(1, 31), random.randint(5, 11))
b = random.sample(range(1, 31), random.randint(5, 11))

print(a)
print(b)
print(list(set(a+b)))
