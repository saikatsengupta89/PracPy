choice='Y'
f1= open("user_input",'w')
while choice=='Y' or choice=='y':
    data= str(input("Enter something you want to write inside the file: "))
    f1.write(data+"\n")

    choice=input('Do you want to continue writing? (Y/N)')
    if (choice=='N' or choice=='n'):
        break
    else:
        continue

f1.close()

print()
print ("The data you have written inside the file is below:")
print()

f2= open("user_input",'r')
for data in f2:
    print (data)

f2.close()