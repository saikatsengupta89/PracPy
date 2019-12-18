#A class will always have attributes and its behaviour
#Attributes are variables which we create and behaviours are the methods
#

class Computer:
    def config (self): #self is the object being passed
        print ("i5, 16gb, 1TB")

com1= Computer()
com2= Computer()

x=9
y='8'

print (type(x))
print (type(y))

print (type(Computer))
print (type(com1))

#multiple ways to call the config method defined inside the class
Computer.config(com1)
Computer.config(com2)

#using the object itself to call the function/method. So, no need to pass the self parameter.
com1.config()
com2.config()

a=5
print(a.bit_length())


