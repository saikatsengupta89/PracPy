# INNER CLASS: INNER CLASS IS A CLASS INSIDE A CLASS
# 1.YOU CAN CREATE OBJECT OF INNER CLASS INSIDE THE OUTER CLASS
# 2.YOU CAN CREATE OBJECT OF INNER CLASS OUTSIDE THE OUTER CLASS PROVIDED YOU USE OUTER CLASS NAME TO CALL IT
class Student:

    def __init__(self, name, rollno):
        self.name= name
        self.rollno= rollno
        self.lap= self.Laptop() #object of laptop (inner class) has to be created inside the outer class

    def show(self):
        print (self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram="8GB"

        def show(self):
            print (self.brand, self.cpu, self.ram)

s1= Student ("Tom",23)
s2= Student ("Harry", 24)

s1.show()
s2.show()
#to create different objects for the inner class we write as below
lap1= s1.lap
lap2= s2.lap
print (id(lap1))
print (id(lap2))

#creating object of a laptop class directly from outside without using the outer class object
lap3= Student.Laptop ()
print (id(lap3))