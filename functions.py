#below example shows python doesn't use pass by value or pass by reference methodolgy to pass arguments to functions
#in python if you change the value of the parameter you pass inside a function that changes the value reference as well
def update (x):
    print(x)
    print(id(x))
    x=8
    print("x : ", x)

a=10;
print(id(a))
update(a)
print("a : ", a)

#below sample shows how to change value in list calling a function
def update_list (x):
    print(x)
    print(id(x))
    x[1]=25
    print(id(x))
    print(x)

a= [10,20,30]
update_list(a)
print(a)

# TYPES OF ARGUMENTS IN PYTHON FUNCTIONS
#actual arguments have four types:
#position
#keyword
#default
#variable length

#passing by position
def add(a,b):
    c=a+b
    print(c)

add(5,6)

#passing by keyword
def person (name, age):
    print(name)
    print(age)

person (age=30, name='Saikat')  #we define the parameters using the keywords as we are not sure of the position

#passing by default
def person (name, age=20):
    print(name)
    print(age)

person ('Saikat')

#passing variable argument to a parameter
#in python you can pass more than one parameter in an argumrnt using * keyword. This will be considered as a tuple
#in below example the first value passed in the parameter will always points to the first parameter
def sum(a, *b):
    c=a
    for i in b:
        c=c+i
    print ("The total sum :", c)

sum(3,5,10,20)

#keyworded variable length arguments in python
#keyworded arguments begins with **

def person (name, **data):
    print(name)
    for i, j in data.items():
        print(j)

person ('Saikat', age=30, sex='Male', phone='0505286231')

#LOCAL AND GLOBAL VARIABLES CONCEPT IN PYTHON

#scenario 1: local and global scope
a=200 #global variable
def something():
    b=100 #local variable
    print("local variable value:", a)
    print("global variable x:", b)

something()
print("global variable value:", a)

#scenario 2: make global variable inside local scope
#you can't access local variable outside of function like below
#print("global variable value:", b)

a=200 #global variable
def something():
    global a #this defines fglobal from inside local scope
    a=100 #local variable
    print("local variable value:", a)

something()
print("global variable value:", a)

#scenario 3: we want to have 'a' local variable  but we also want to change the global variable 'a'
a=10
b=20
c=30
print(id(a))

def change_global():
    a=50
    x= globals()['a']
    print(id(x))
    print(a)
    globals()['a']=30  #changing the global variable value from inside local scope

change_global()
print(a)


#PASSING LIST TO A FUNCTION IN PYTHON



#CREATING FACTORIAL FUNCTION USING PYTHON
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

fact_result= fact(5)
print("factorial of 5 :",fact_result)