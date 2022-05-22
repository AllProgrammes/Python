with open("poem.txt", "r") as f:
    data_copy = f.read()
    if "twinkle" in data_copy:
        print("Yes,The word twinkle is present in the file(poem.txt)")
    else:
        print("No,The word twinkle is not present in the file(poem.txt)")
