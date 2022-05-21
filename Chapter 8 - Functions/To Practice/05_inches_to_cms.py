def converter(inchs):
    cms = inchs * 2.54
    return cms


inchs = float(input("Enter measurement in inchs here : "))
print(inchs, "Inch =", converter(inchs), "cms")
