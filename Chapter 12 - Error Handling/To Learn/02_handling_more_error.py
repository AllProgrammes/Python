a = input("Enter any number : ")
try:
    a = int(a)
    c = 1 / a
    print(c)
except ValueError:
    print(
        "\nA value error occured *_*\nMake sure you have entered a valid value"
    )  # if we divide any number by [harry] then it will generate a value error because it harry is not acceptable XD
except ZeroDivisionError:
    print(
        "\nA ZeroDivisionError occured *_*\nMake sure you are not dividing by zero"
    )  # if we divide any number by zero then it will generate the ZeroDivisionError
except:
    print("\nHmmmmmm !! So you entered something physy\nPlease check your input :)")

print("\n\nThanks for using this program ^_^\n\n")
