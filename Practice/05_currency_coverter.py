"""
Steps to use this currenct converter :-
1. Go to this website https://www.x-rates.com/table/?from=INR&amount=1
2. Copy the table a far as you want 
3. Make a txt file named "currency_database.txt" and paste the data thier
4. Now Download this program  in same place where you made your txt file.
5. Run this program in your terminal
6. Enjoy

"""


import fontstyle

# WELCOME
print(
    fontstyle.apply(
        "\n\n========================================================================WELCOME TO CURRENCY CONVERTER===================================================================================",
        "red,bold,yellow_bg",
    )
)

# OPENING THE DATABASE FILE FOR STARTING THE PROGRAM
try:  # TRYING TO OPEN THE FILE
    with open("currency_database.txt") as f:
        lines = f.readlines()
        currency_dict = {}
        for line in lines:
            parsed = line.split("\t")
            currency_dict[parsed[0]] = parsed[1]
        print(
            fontstyle.apply(
                "\n\nHere the available list of currencies in this program",
                "blue,bold,underline",
            ),
            ":-\n",
        )

        # temp_list=list(currency_dict.keys())
        # temp_list="\n".join(temp_list)
        # print(temp_list)
        # All these in one command --> print("\n".join(list(currency_dict.keys())))
        print(fontstyle.apply("\n".join(list(currency_dict.keys())), "blue"))
        print(
            "\nNote : \n1.This program is case sensative\n2.Press 'q' to exit anytime !!"
        )
        while True:
            # takes values as string
            user_amount = input(
                fontstyle.apply(
                    "\nEnter the amount[in INR] you want to convert : ", "green"
                )
            )

            # To stop program when q is entered
            if user_amount == "q" or user_amount == "Q":
                print(
                    "\n\n",
                    fontstyle.apply(
                        "\t\t\t\t\t\t\t\tThanks for choosing my CURRENCY CONVERTER ^_^",
                        "red,bold,yellow_bg",
                    ),
                )
                break

            # takes values as string
            user_demand = input(
                fontstyle.apply(
                    "Enter the name of the currency name in which you want to convert : ",
                    "green",
                )
            )

            # To stop program when q is entered
            if user_demand == "q" or user_demand == "Q":
                print(
                    "\n\n",
                    fontstyle.apply(
                        "\t\t\t\t\t\t\t\tThanks for choosing my CURRENCY CONVERTER ^_^",
                        "red,bold,yellow_bg",
                    ),
                )
                break

            try:
                user_amount = float(
                    user_amount
                )  # tries to convert the string into float form and if it fails to do so then prints the except part
                if (
                    currency_dict.get(user_demand) == None
                ):  # what if user enters somthing which is not is not in the currency list
                    print(
                        fontstyle.apply(
                            "\nPlease enter a currency from the above list !!",
                            "red,bold",
                        )
                    )
                    continue
                else:
                    value_of_the_currency = float(currency_dict.get(user_demand))
                print(
                    fontstyle.apply(
                        f"Value of {user_amount} INR in {user_demand} at rate of {value_of_the_currency} per INR is --> {value_of_the_currency*float(user_amount)}",
                        "black_bg,white,bold",
                    )
                )
            except:  # for handling other types of error
                print(fontstyle.apply("\nPlease enter a valid input !!", "red,bold"))

# BUT WHAT IF THE DATABASE FILE IS NOT FOUND
except (FileNotFoundError, IOError):
    print(
        fontstyle.apply(
            "Error : Database file is missing or in the wrong path\nSoltion : Keep the database file in that same directory where you are running this program or check if the database file is named as 'currency_database.txt'",
            "red,bold",
        )
    )
