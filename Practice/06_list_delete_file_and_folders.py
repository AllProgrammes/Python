import os
import shutil
from time import sleep
import fontstyle

cwd = os.getcwd()
dir = os.listdir()
print(fontstyle.apply(f"ATTENTION !\nCurrent working directory is : {cwd}", "red,bold"))
print(
    fontstyle.apply("\nFiles in this Directory are", "blue,underline"),
    fontstyle.apply(" :-", "blue"),
)
print(fontstyle.apply("\n".join(dir), "blue"))

file = input("Enter the name of the file which you want to delete : ")
path = os.path.join(cwd, file)
try:
    print("Searching for file", end="")
    for i in range(10):
        print(".", end="")
        sleep(0.2)
    if os.path.exists(file) == True:
        print("Found !!")
        type = input(
            "What file type it is ?\nPress '1' for Folder or press any key if it is single file : "
        )
        print("Deleting file", end="")
        for i in range(10):
            print(".", end="")
            sleep(0.2)
        size = os.path.getsize(file)
        if type == "1":
            shutil.rmtree(path)
        else:
            os.remove(file)
        print("Deleted !!")
        print(f"{size} bytes of disk memory freed")
    else:
        print("File not found !!😐 ")
except Exception as error:
    print(f"Deletion Failed !!\nError : {error}")
