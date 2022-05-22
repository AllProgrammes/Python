data = True
search = input("Enter for what do you want to search for in log file : ")
print("\n")
i = 0
count = 0
with open("log.txt", "r") as f:
    while data:
        data = f.readline()
        if search.lower() in data.lower():
            count += 1
            print(data)
            print(
                "Yes, Log for",
                search,
                "is present in log file at line number",
                i,
            )
        i += 1

if count == 0:
    print("No, Log for", search, "is not present in log file")
