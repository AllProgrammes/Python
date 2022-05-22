f = open("test.txt")

# read first line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# read third line and so on
data = f.readline()
print(data)

f.close()  # important
