n = 3
for row in range(1, n + 1):
    if row == 2:
        print("x " * 1, end="")
        print("  " * 1, end="")
        print("x " * 1)
        continue
    print("x " * n)
