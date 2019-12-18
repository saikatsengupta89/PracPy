# OBJECTS WILL HAVE TWO THINGS: VARIABLES AND METHODS. VARIABLES TO STORE DATA AND METHOD FOR BEHAVIOURS
# TYPES OF METHODS: 1. INSTANCE METHOD 2. CLASS METHOD 3. STATIC METHOD
# INSTANCE METHODS: WORKS WITH INSTANCE VARIABLES.
# TWO TYPES OF INSTANCE METHODS: 1. ACCESSORS/ GETTER METHODS  2. MUTATOR/ SETTER METHODS
# STATIC METHODS: METHODS WHICH IS NOT RELATED TO THE CLASS. I.E. THEY DON'T USE CLASS/INSTANCE VARIABLES
# STATIC METHODS ARE KEPT FOR SOME COMMON USE LIKE SAY YOU HAVE A FACTORIAL METHOD. NOT RELATED TO ANYTHING

class Student:

    school="Methodist"

    #INSTANCE METHOD
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #INSTANCE METHOD
    def avg(self):
        return (self.m1+ self.m2+ self.m3)/3

    # GETTER/ACCESSOR METHOD
    def getM1(self):
        return self.m1

    # SETTER/MUTATOR METHOD
    def setM1(self, m1):
        self.m1= m1

    # CLASS METHOD ACCESSING CLASS VARIABLE -> school
    @classmethod   # THIS IS A DECORATOR. iT IS PASSED SO THAT WHEN WE CALL THE CLASS METHOD WE NEED NOT PASS cls INSIDE
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def info():
        print ("This is class Student")

s1= Student (80,40,20)
s2= Student (90, 50,60)

print ("Student1 average: ",s1.avg())
print ("Student2 averageL ",s2.avg())

s1.setM1(30)
print ("Marks 1 for Student 1: ", s1.m1)

print (Student.getSchoolName()) #if decorator is not defined, this will throw error and we need to print: Student.info(Student)
Student.info()
