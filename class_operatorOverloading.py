class Student:

    def __init__(self, m1, m2):
        self.m1= m1
        self.m2= m2

    # method overloading: defining __add__ as per the object addition requirement
    def __add__(self, other):
        m1= self.m1+ other.m1
        m2= self.m2+ other.m2

        s3= Student(m1,m2)
        return s3

    # method overloading: defining __mul__ as per the object multiplication requirement
    def __mul__(self, other):
        m1= self.m1* other.m1
        m2= self.m2* other.m2

        s3= Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1= self.m1+ self.m2
        r2= other.m1+ other.m2
        if (r1> r2):
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1= Student(30,40)
s2= Student(60,20)

print ("Addition overloading")
s3=s1+s2
print ("Total Marks for m1 :", s3.m1)
print ("Total Marks for m2 :", s3.m2)

print ("Multiplication overloading")
s3= s1*s2
print ("Total Marks for m1 multiplied :", s3.m1)
print ("Total Marks for m2 multiplied :", s3.m2)

print ()
print ("Compare two student objects based on narks obtained")

if s1 > s2:
    print ("Student 1 wins")
else:
    print ("Student 2 wins")

# after overloading the __str__ method, when you print the object, it prints the variable values of the object instead of the address
print (s1)