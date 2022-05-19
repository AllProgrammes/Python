a = [1, 2, 3, 4, 5]
print(a[1])  # prints the value on that index only
print(a)  # prints the whole list

a[0] = 56  # we can change like this also
print(a)

b = [69, "Biswajit", 56.67, True]  # a list can contain various types of values
print(b)

friends = ["Shreya", "Sujal", "Anubhav"]
print(friends[0:])  # prints all friends name from index 0 to 2
print(friends[-3:])  # totally same as friends[0:3] or friends[0:]
