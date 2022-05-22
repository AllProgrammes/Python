with open("log.txt", "r") as f:
    data = f.read()
    search = input("Enter for what do you want to search for in log file : ")
    if search in data:
        print("Yes, Log for", search, "is present in log file")
    else:
        print("No, Log for", search, "is not present in log file")
