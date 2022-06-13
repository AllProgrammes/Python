sqaure = lambda num: num * num

numbers = [3, 5, 6]

# Approach 1
new_list = []
for item in numbers:
    new_list.append(sqaure(item))

print(new_list)

# Approach 2
print(
    list(map(sqaure, numbers))
)  # here we have typcasted into list because it was returning non_readble values like this --> <map object at 0x00000205B44BAFE0>
