from time import sleep


for i in range(1, 5):
    try:
        print(f"Searching for 01_file{i}.txt", end="")
        for temp in range(10):
            print(".", end="")
            sleep(0.3)
        file_test = open(
            f"01_file{i}.txt"
        )  # by default all files are opened in read mode if not mentioned
        print(f"File was found !")
    except:
        print(f"01_file{i}.txt was not found")
