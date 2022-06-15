import fontstyle

print(
    fontstyle.apply(
        "\n\n========================================================================WELCOME TO APNA KIRANA STORE====================================================================================",
        "red,bold,yellow_bg",
    )
)
print("\n\nPress 'q' to quit anytime\n")
sum = 0
counter = 1
while True:
    try:
        price = input("Enter the Price of the item : ")
        if str(price) == "q" or str(price) == "Q":
            counter -= 1
            print(fontstyle.apply(f"Price of {counter} items is {sum}", "green,bold"))
            print(
                fontstyle.apply(
                    "\n\n\t\t\t\t\t\t\t\tThanks for choosing APNA KIRANA STORE ^_^",
                    "red,bold,yellow_bg",
                )
            )
            break
        else:
            sum = sum + int(price)
            counter += 1
            print(f"Order Total till now --> {sum}\n")
    except ValueError:
        print("Please enter a valid value !!")
