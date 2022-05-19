data = input("Enter the sentance/paragraph below : ")
print(
    "Working on your data......\nFound",
    data.count("  "),
    "double spaces\nRemoving extra spaces.....\n\nDone!\n",
)
print(data.replace("  ", " "))
