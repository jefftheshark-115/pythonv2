from random import random, randint, randrange
c = 0
for i in range(100000):
    x = random()
    if x < 0.0001:
        c += 1
print(f"Number of times x < 0.0001: {c}")