# database
DATABASE = (("a", "@"), ("and", "&"), ("i", "|"), ("x", "*"), ("c", "("), ("s", "$"))

# function
def secure_password(password):
    for a, b in DATABASE:
        password = password.replace(a, b)
    return password


# main file runner
if __name__ == "__main__":
    password = input("Enter your password here : ")
    print("Your secure password is", secure_password(password.lower()))
