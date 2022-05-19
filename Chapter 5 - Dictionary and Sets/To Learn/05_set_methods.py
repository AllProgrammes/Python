# Adding values to empty sets
a = set()
a.add(5)
a.add(2)
a.add(6)
a.add(5)
print(type(a))
print(a)

# Length of set a
print("The lenght of set 'a' is", len(a))

# Removing a value from set a
print("Removing 5 from set 'a'.....\nAfter removing 5 from the set the set is now")
a.remove(5)
print(a)

# Clearing a set
a.clear()
print(a)

# Union of sets
a = {3, 4, 5, 6}
b = {1, 2, 7, 3}
print(a.union(b))

# Intersection of sets
print(a.intersection(b))
