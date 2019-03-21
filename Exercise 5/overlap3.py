# Exercise 5 List Overlap
# Extra 1 alt

import random

a = random.sample(range(1, 31), random.randint(5, 21))
b = random.sample(range(1, 31), random.randint(5, 21))

c = set(a + b)
d = list(c)
print(d)
