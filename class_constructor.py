# BELOW WE WILL DISCUSS THE CONSTRUCTOR, SELF AND OBJECT COMPARISON
# WHENEVER WE CREATE A CLASS AND WE INSTANTIATE AN OBJECT, THE OBJECT IS CREATED AND ALLOCATED SPACE
# SIMILARLY IF N NO OF OBJECTS ARE CREATED, THEY ARE ALLOCATED SPACE 'N' NO OF TIMES
# SIZE OF AN OBJECT?
# DEPENDS ON THE NUMBER OF VARIABLES AND SIZE OF EACH VARIABLE
# WHO ALLOCATE SIZE TO OBJECT?
# CONSTRUCTOR. THE CONSTRUCTOR WILL CALL THE INIT METHOD FOR YOU TO ALLOCATE MEMORY
#

class MyClass:
    def __init__(self):
        self.name="Saikat"
        self.age=30

    def update(self):  #this is defined self so that the update function knows which object to do an update while called
        self.age=32

    def compare (self, other):
        if self.age==other.age:
            return True
        else:
            return False

c1= MyClass() #calling the constructor of the class
c2= MyClass() #calling the constructor of the class

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

#below statement will compare the two objects
if c1.compare(c2):
    print ("They have same age")
else:
    print ("They have different age")


# this will update the age variable for whichever object is called
print("After age update done on one of the object")
c2.update()

print(c1.age)
print(c2.age)

#below statement will compare the two objects
if c1.compare(c2):
    print ("They have same age")
else:
    print ("They have different age")