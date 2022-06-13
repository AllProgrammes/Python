from functools import reduce
import random


random_numbers = []

# Generates 5 random int values between 1 to 100 into the enpty list
for i in range(5):
    temp = random.randint(1, 100)
    random_numbers.append(temp)

print(random_numbers)

# Approach 1
# print(max(random_numbers))

# Approach 2
temp = reduce(max, random_numbers)
print(temp)
