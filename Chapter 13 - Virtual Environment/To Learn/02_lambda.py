# def add_five(num):
#     return num+5

# It does the same work as def fx shown above
add_five = lambda num: num + 5
print("After adding 5 to 65 , it becomes", add_five(65))

# we can give more than one argument to lamda function
add_three_numbers = lambda x, y, z: x + y + z
print("The sum of 1,2 and 5 is", add_three_numbers(1, 2, 5))
