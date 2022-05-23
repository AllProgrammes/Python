class Employee:
    company = "awaken"

    def getsalary(self):
        print(f"Salary for employee working at {self.company} is {self.salary}")


biswajit = Employee()
biswajit.salary = "Rs 100000"
biswajit.getsalary()

# biswajit.salary()-----gets converted into this----->Employee.salary(biswajit)
# hence the error --> [Employee.salary() takes 0 positional arguments but 1 was given]
