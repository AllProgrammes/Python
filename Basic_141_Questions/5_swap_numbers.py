a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

# Swap using 3rd variable
c = a
a = b
b = c
print(f"After swapping a is {a} and b is {b}")

# Swap without using 3rd variable
b = a*b
a = b//a
b = b//a
print(f"After swapping a is {a} and b is {b}")
