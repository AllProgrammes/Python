import os
import time

files = os.listdir()  # stores all file
binod_files = []  # stores file names which have binod in it


def binod_detector(file):
    with open(file) as f:
        a = f.read()
        if "binod" in a.lower():
            binod_files.append(file)


# welcome
print(
    "\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx WELCOME TO BINOD DETECTOR xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)
print(f"\n\nCurrent directory is : {os.getcwd()}\n")
print("Searching for BINOD in files", end="")

# wait time animation
for i in range(11):
    print(".", end="")
    time.sleep(0.5)

# file sorting
for file in files:
    if os.path.isfile(file) == True:
        if file.endswith("txt"):
            binod_detector(file)

# final output
print(f"Done !!\nFound Binod in {len(binod_files)} files")
