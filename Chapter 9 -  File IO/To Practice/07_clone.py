with open("poem.txt") as f:
    cpy = f.read()

with open("this.txt", "w") as f:
    f.write(cpy)
