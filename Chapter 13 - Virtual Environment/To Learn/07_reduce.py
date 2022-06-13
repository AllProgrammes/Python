from functools import reduce


find_sum = lambda a, b: a + b
numbers = [1, 2, 3, 4]
temp = reduce(find_sum, numbers)
print(temp)

"""
Q.     So what reduce(find_sum, numbers) does ?
Ans :  it keep on doing sum of 2 numbers by taking numbers from left to right of the list like -->
        
        round 1 : it takes 1 and 2 and gives a list like [3,3,4]
        round 2 : it takes 3 and 3 and gives a list like [6,4]
        round 3 : it takes 6 and 4 and gives a list like [10]
        
"""
