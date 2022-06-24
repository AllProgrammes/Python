def check_armstrong(number):
    sum = 0
    order = len(str(number))
    while number != 0:
        digit = number % 10
        sum += pow(digit, order)
        number = number // 10
    return sum


"""
Explanation :

    Lets suppose the number is 153  then 
    round 1 :
            digit=153 % 10 
            digit will save the remainder which is 3 here
            then sum will store the digit^number_of_digits value which is 27 here
            then number will get divided by 10 and the value is saved in number itself i.e 15
    round 2 :
            digit=15 % 10 
            digit will save the remainder which is 5 here
            then sum will store the digit^number_of_digits value which is 27+125 here
            then number will get divided by 10 and the value is saved in number itself i.e 1
    round 3 :
            digit=1 % 10 
            digit will save the remainder which is 1 here
            then sum will store the digit^number_of_digits value which is 27+125+1 here
            then number will get divided by 10 and the value is saved in number itself i.e 0 and after which this loop will end itself
"""


if __name__ == "__main__":
    while True:
        number = input("Enter a number : ")
        try:  # what if user enter his/her name
            number = int(number)
            if check_armstrong(number) == number:  # quick check
                print(f"{number} a armstrong number.")
            else:
                print(f"{number} not an armstrong number.")
        except Exception:
            print("Enter a valid input !!")
