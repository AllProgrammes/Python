import os

oldname = "test.txt"
newname = "renamed.txt"
with open(oldname) as f:
    data = f.read()

os.rename(oldname, newname)

with open(newname, "w") as f:
    f.write(data)

with open("rename_check.txt", "w") as f:
    f.write(data)
