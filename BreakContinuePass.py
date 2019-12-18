#to showcase break statement
x= int(input("How many candies you want? "))
available_candies=5
i=1
while (i<=x):
    print ("Candy")
    i=i+1
    if (i>available_candies):
        print("There were only 5 candies available")
        break
print("Bye")

#print all values from 1 to 100 but skip those are divisible by 3
#to showcase continue statement
for i in range(1,101):
    if (i%3==0):
        continue;
    print (str(i)+" ", end="")
print()

#print all values from 1 to 100 but not the odd numbers
#to showcase pass statement
for i in range(1,100):
    if (i%2==0):
        print (str(i)+" ", end="")
    else:
        pass
print()
