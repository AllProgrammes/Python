def converter(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit


celcius = float(input("Enter temperature in celcius here : "))
print(celcius, "Celcius =", converter(celcius), "Fahrenheit")
