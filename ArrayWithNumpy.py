from numpy import *  #package used to create multi-dimensional arrays. not supported in base package

# inside numpy you can create arrays in six different ways
# 1. array()  2.linespace()  3.logspace()  4.arange()  5.zeros()  6.ones()
#
arr= array([1,2,3,4,5]) #you can define an array without specifyingb the type
print(arr)

arr= array([1,2,3,4,5],int) #but if you want you can specify in the end like this
print(arr)

arr= array([1,2,3,4,5.0])
print(arr.dtype)
print(arr)

arr= linspace(0,15,16) #basically the range 0 to 15 is divided into 16 parts. You can divide it to as many parts
print (arr)

arr=linspace(0,15)  #this will create parts by itself and it can be many depending on the range you provided
print (arr)

arr=arange(0,15,2)
print(arr)

arr=logspace(1,40,5)  # will divide 10 raised to 1 upto 10 raised to 40 n 5 parts
print(arr)


#various operations you can perfrom using numpy

arr1= array([1,2,3,4,5])
arr2= array([6,7,8,9,10])


print(squeeze(arr1+5))
print(max(arr1))
print(min(arr1))
print(sqrt(arr1))
print(squeeze(arr1))
print(concatenate([arr1, arr2]))

#copyin one array to another
arr3= arr1

#both array below will have the same address
print ("Array 1 address: "+ str(id(arr1)))
print ("Array 2 address: "+ str(id(arr3)))


#shallow copy
print ("********************shallow copy**********************")
arr1= array([1,2,3,4,5])
arr3= arr1.view() #view opertion creates an array with elements of the copied array but as a new array and not pointing to the old one

#both array below will have different address now
print ("Array 1 address: "+ str(id(arr1)))
print ("Array 2 address: "+ str(id(arr3)))

arr1[2]=15  # this operation changes element for both the arrays. That's why shallow copy
print("Array 1 :"+ str(arr1))
print("Array 3 :"+ str(arr3))
print ("Array 1 address: "+ str(id(arr1)))
print ("Array 2 address: "+ str(id(arr3)))


#deep copy
print ("********************deep copy**********************")
arr1= array([1,2,3,4,5])
arr3= arr1.copy() #view opertion creates an array with elements of the copied array but as a new array and not pointing to the old one

#both array below will have different address now
print ("Array 1 address: "+ str(id(arr1)))
print ("Array 2 address: "+ str(id(arr3)))

arr1[2]=15  # this operation will change element for arr1 only and not for arr3. That's why deep copy
print("Array 1 :"+ str(arr1))
print("Array 3 :"+ str(arr3))
print ("Array 1 address: "+ str(id(arr1)))
print ("Array 2 address: "+ str(id(arr3)))

#two dimensional array
print ("******************2D array*********************")
arr1= array ([
              [1,2,3,4,5,6],
              [7,8,9,10,11,12]
             ])
print(arr1)
print("No of dimensions: "+ str(arr1.ndim))
print("Shape: "+ str(arr1.shape))
print("Type: "+ str(arr1.dtype))

arr2= arr1.flatten() #flttens the 2D array into a single dimensional array
print(arr2)

arr3= arr2.reshape (4,3)
print(arr3)

arr4= arr2.reshape(2,2,3)
print(arr4)

print("*******************Multidimensional Matrix*****************")
arr1= array([
    [1,2,3,4],
    [5,6,7,8]
])

m= matrix(arr1)
print(m)

#another way of defining matrix is as below
m= matrix('1,2,3;4,5,6;7,8,9')
print(m)
#to print all the diagonal elements of the matrix
print(diagonal(m))
print (m.max())

#multiply two matrices as shown below
