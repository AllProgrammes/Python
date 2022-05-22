class Employee:
    company = "Awaken"


cosmos = Employee()
aurora = Employee()
print("Company =", cosmos.company)
print("Company =", aurora.company)

Employee.company = "Pixel Experience"
print("Company =", cosmos.company)
print("Company =", aurora.company)
