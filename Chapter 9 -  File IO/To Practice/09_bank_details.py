run = True
count = 1
store = open("bank_details.txt", "w")
store.write(
    "S No.                  Account Holder Name                 Account Number                  Account Balance\n"
)
while run == True:
    print(f"\nIndex {count}")
    name = input("Enter Account holder name : ")
    account_number = input("Enter the account number : ")
    account_balance = input("Enter account balance : ")
    if len(name) == 15:
        store.write(
            f"{count}                      {name}                      {account_number}                       {account_balance}\n"
        )
    elif len(name) == 13:
        store.write(
            f"{count}                      {name}                        {account_number}                       {account_balance}\n"
        )
    elif len(name) < 13:
        store.write(
            f"{count}                      {name}                            {account_number}                       {account_balance}\n"
        )
    if count % 5 == 0:
        choice = input(
            "If you want to exit press 'Y' else press any key to continue : "
        )
        if choice == "Y" or choice == "y":
            store.close()
            break
        else:
            continue
    count += 1
