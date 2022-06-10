# This my friend is a global variable
global_variable = "I am 69"


def print_variable():
    # This my friend is not a global variable
    global_variable = "I am not 69"
    print(global_variable)


print(global_variable)
print_variable()
