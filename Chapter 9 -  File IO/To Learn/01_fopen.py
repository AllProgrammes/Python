# by this way we can read the content of a file anf print it
f = open("test.txt")  # by defalut the mode is r--> read
data = f.read()
# data = f.read(5)by this way we can specify the number characters we want to print
print(data)
f.close()
