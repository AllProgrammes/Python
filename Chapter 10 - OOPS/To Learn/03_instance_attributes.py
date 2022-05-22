class Employee:
    company = "Awaken"
    salary = "69$"


cosmos = Employee()
aurora = Employee()
print("Company =", cosmos.company)
print("Salary =", cosmos.company)

# prints default what's given in class Employee
print("Company =", aurora.salary)
print("Salary =", aurora.salary)

# but if we do like this then it will override the default values
cosmos.salary = "99$"  # yes more salary because I dont have wifi
aurora.salary = "89$"
print("\nAfter defining")
print("Company =", aurora.salary)
print("Salary =", aurora.salary)
