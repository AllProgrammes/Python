from time import sleep


all_numbers = [2, 3, 6, 7, 8, 10, 45, 67]
count = 0
print("Starting", end="")
for i in range(10):
    print(".", end="")
    sleep(0.2)

for item in all_numbers:
    if item % 2 == 0:
        count += 1
        if count == 1:
            print(f"\nFound an even Number")
            sleep(0.5)
        else:
            print("Again Found an even Number")
            sleep(0.5)
        # even_numbers.append(item) --> can be written as follows 👇

# Shortcut method
# reason --> if we do this the we don't have to do that above for loop shit -_-
even_numbers = [i for item in all_numbers if item % 2 == 0]

print(f"Total {count} even numbers have been found")
print(f"\nEven numbers are {even_numbers}")
