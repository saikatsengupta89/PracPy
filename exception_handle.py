#THERE ARE THREE KIND OF ERRORS:
#1. COMPILE TIME ERROR (mostly syntactical errors)
#2. LOGICAL ERROR (in logical error the code gets compiled and it also produces output, but it's not correct output)
#3. RUNTIME ERROR (the code compiles properly, there are no syntactical error, but for certain combination of user input it throws error while processing)
print ("Open Connection")
print ("Lets divide two numbers")
try:
    a= int (input ("Enter numerator : "))
    b= int (input ("Enter denominator : "))
    c=float(a/b)
    print ("Division result : ", c)

except ValueError as e:
    print ("Input format should be integer. ", e)

except ZeroDivisionError as e:
    print ("Denominator can't be zero")

except Exception as e:
    print ("Exception thrown : ", e)

# finally block executes whether there is any error or no error
# in real time scenario, to close any connections which has been opened earlier or any mandatory operations
# should be performed inside this block.
finally:
    print ("Close Connection")

