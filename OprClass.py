class Employee:
    def __init__(self, name, department, age):
        self.name= name
        self.department= department
        self.age= age

    def workStation(self):
        print("Workstation :" + " Abu Dhabi, UAE")

p1= Employee ("Saikat", "IT", 30)
print("Employee name : "+ p1.name)
print("Employee department : "+ p1.department)
print("Employee age : "+ str(p1.age))
p1.workStation()