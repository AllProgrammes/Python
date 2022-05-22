with open("film.txt", "r") as f:
    data = f.read()
    print("Your lines are :")
    print(data)

with open("film.txt", "w") as f:
    print("\nStarting censor board program.....\n")
    data = data.replace("donkey", "######")
    f.write(data)
    print("Censored Lines :")
    print(data)
