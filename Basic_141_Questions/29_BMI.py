def BMI(weight,height):
    return weight/height**2

weight = int(input("Enter your weight(kg) : "))
height = int(input("Enter your height(cm) : "))
height/=100

if(BMI(weight,height)<=18.5):
    print("You are underweight")
elif(18.5<BMI(weight,height)<=24.9):
    print("Your weight is normal")
elif(25<BMI(weight,height)<=29.29):
    print("Your are overweight")
else:
    print("You are obese")