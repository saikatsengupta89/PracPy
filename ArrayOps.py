from array import *


vals =array ('i',[5,6,7,8,9])
vals.reverse()
print (vals)

# there are two ways to print all the elements in an array
#Way 1:
for i in vals:
    print (str(i)+" ", end="")
print()

#Way 2:
for i in range(len(vals)):
    print (str(vals[i])+" ", end="")
print()

vals= array('u',['a','e','i','u','o'])
for i in vals:
    print(i+" ", end="")
print()

#creating a new array from another existing array- copying one array from another
newArray= array(vals.typecode, (i for i in vals))
for i in newArray:
    print(str(i)+" ", end="")


#appending values to array andthen displaying the one element which is searced for
print ("******************creating a new array of your choice********************************")
arr= array('i',[])  #define an enmpty array at the first place
arr_length= int(input("Enter the no. of elements you need to add in the array "))
print("Enter elements below")

for i in range(arr_length):
    ele= int(input("Enter element "+str(i+1)+" : "))
    arr.append(ele)

print ("The array you have created:")
print (arr)

print("*******************search lement inside the array created*****************************")
ele=int(input("enter the element to search: "))
for i in arr:
    if (i==ele):
        print ("The element is available at index :"+ str(arr.index(i)))
        break


