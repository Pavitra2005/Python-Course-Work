class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def cal_annual_salary(self):
        return self.base_salary*12


# Object creation
emp = Employee("John", 35000)
print("Annual Salary:", emp.cal_annual_salary())
