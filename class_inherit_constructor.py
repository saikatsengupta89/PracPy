# IF YOU CREATE OBJECT OF SUB CLASS IT EILL FIRST TRY TO FIND INIT OF SUB CLASS
# IF IT IS NOT FOUND THEN IT WILL CALL INIT OF SUPER CLASS
#

class A:
    def __init__(self):
        print ("This is from constructor A")

    def feature1(self):
        print ("Feature1A is working fine")

    def feature2(self):
        print ("Feature2 is working fine")

class B:
    def __init__(self):
        print ("This is from constructor B")

    def feature1(self):
        print ("Feature1B is working fine")

    def feature3(self):
        print ("Feature3 is working fine")

    def feature4(self):
        print ("Feature4 is working fine")

class C (A,B):
    def __init__(self):
        super().__init__()  #calling the init of super class
        print ("This is from constructor C")

    #calling method of super class from subclass
    def feature(self):
        super().feature2()

# by default the below statement will create an instance for class B and will call the constructor of class A
# if there is no constructor defined for class B
b= B()

#below instance creation will call the __init__ of super class A and not B. This is due to MRO (Method Resolution Order)
#whenever you have multiple class inheritance, the child class will always look up to that parent class which comes left
#it will always start from left to right.
c=C()
c.feature1()
c.feature()


