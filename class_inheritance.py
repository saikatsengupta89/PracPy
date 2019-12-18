# THERE ARE TWO TYPES OF INHERITANCE: 1. SINGLE INHERITANCE 2. MULTIPLE INHERITANCE

class A:
    def feature1(self):
        print ("Feature1 is working fine")

    def feature2(self):
        print ("Feature2 is working fine")

class B:
    def feature3(self):
        print ("Feature3 is working fine")

    def feature4(self):
        print ("Feature4 is working fine")

class C (A, B):
     def feature5(self):
         print ("Feature5 is working fine")

class D (A):
    def feature6 (self):
        print ("Feature6 is working fine")


#creating an instance of class B below. B can only access feature of class A
d= D()
d.feature1()
d.feature2()
d.feature6()
print()
# creating an instance of class C below. The instance is able to access all features of both (A,B). This is multiple inheritance
c= C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
