class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        average=sum(self.marks)/len(self.marks)
        return average >=40
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)
        print("Passed:",self.is_passed())

stu=Student("Pooji",[45,55,69])
stu.display()

