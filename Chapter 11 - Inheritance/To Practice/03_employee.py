class employee:
    salary = 5000
    increment = 700

    @property
    def salaryafterincrement(self):
        return self.increment + self.salary

    @salaryafterincrement.setter
    def salaryafterincrement(self, total_salary):
        self.increment = total_salary - self.salary


raju = employee()
raju.salaryafterincrement = 6000
print(raju.salaryafterincrement, "=", raju.increment, "+", raju.salary)
