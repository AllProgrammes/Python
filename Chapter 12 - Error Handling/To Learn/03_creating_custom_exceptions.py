def take_mobile_number(mobile_number):
    try:
        mobile_number = int(mobile_number)
        print("Your mobile number is", mobile_number)
    except:
        raise ValueError("Please enter a valid mobile_number -_-")


mobile_number = input("Enter your mobile number : ")
take_mobile_number(mobile_number)
