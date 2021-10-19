#Write a program that calculates the circumference of a wheel. The formula is C=2πr, where π is the value 3.14 and r is the radius of the circle.

import math, random

# We can generate a random number using the randint method

random_number = random.randint(0,10)
#randint show range
cirmc = 2 * math.pi * random_number
print(cirmc)
