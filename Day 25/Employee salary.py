class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_annual_salary(self):
        return self.base_salary * 12
    def display(self):
        print("name:",self.name)
        print("base_salary:",self.base_salary)


emp = Employee("John", 35000)
emp.display()
print("Annual Salary:", emp.calculate_annual_salary())






