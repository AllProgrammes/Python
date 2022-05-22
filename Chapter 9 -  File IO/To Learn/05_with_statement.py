with open("with.txt", "w") as f:
    f.write("Hello Peter !!")

with open("with.txt") as f:
    copydata = f.read()
    print(copydata)

# so why to use with statement ?
# because with (with) statement we dont have to close the file manually by writing f.close()
