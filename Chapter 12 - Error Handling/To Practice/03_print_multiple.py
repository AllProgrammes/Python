user_number = input("Enter the number which you want to get the table : ")
try:
    user_number = int(user_number)
    multiples = [user_number * i for i in range(1, 11)]
    print(multiples)
except:
    print("Please enter a number ＞﹏＜")
