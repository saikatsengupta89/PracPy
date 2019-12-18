#method overloading is not supported in python.
#we use alternate tricks to perform method overlodaing inside a same class as shown below
class sumAll:
    def __init__(self):
        pass
#********************METHOD OVERLOADING CONCEPT BELOW******************************
    #python type of method overloading
    def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s= a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
#***********************METHOD OVERRIDING CONCEPT BRLOW*******************************
class A:
    def show(self):
        print ("in A Show")

class B(A):
    pass

class C(A):
    def show(self):
        print ("in C show")

s1= sumAll()
s= s1.sum(30,20,40)
print ("Sum of three numbers passed:", s)

s=s1.sum(50)
print ("Sum of one number passed:", s)

#in method overriding, when the method is not existing in the child class like show() method below, it calls the parent one
b= B()
b.show()
#but if the show() method is defined in the child class, it overrides the same method of the parent class like below
c=C()
c.show()