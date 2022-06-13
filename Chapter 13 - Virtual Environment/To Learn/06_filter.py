# Filter Syntax
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


greater_than_10 = lambda num: num > 10


numbers = [1, 2, 34, 5, 6, 7]
print("Number which are greater than 5 are ", list(filter(greater_than_5, numbers)))
print("Number which are greater than 10 are ", list(filter(greater_than_10, numbers)))
