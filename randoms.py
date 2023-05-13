# askpython.com - For details of python modules
import random as rand

print(rand.randint(1, 8))  # Between 1 & 8 included [min, max]
rand.random()  # Float btwn 0 & 1 not including 1 [0, 1)

# Random pick from a list
rand.choice(["a", "b", "c", "d"])

# Shuffling
rand.shuffle([1,2,3,4])