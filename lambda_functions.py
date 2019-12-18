from functools import reduce

# IN PYTHON ANONYMOUS FUNCTIONS ARE CALLED LAMBDA FUNCTIONS
# HERE THE FUNCTION HAS A BODY BUT IT DOESNOT HAVE A NAME
# THE WAY WE PASS VALUES OR THE WAY WE PASS OBJECTS, WE CAN SIMILARLY PASS FUNCTIONS
# FUNCTIONS ARE OBJECTS IN PYTHON

f= lambda x: x*x
y= lambda a,b: a+b

res1= f(5)
res2= y(10,20)

print(res1)
print(res2)

#below demonstration will show use of filter, map, reduce operations in python using lambda functions
#1.Take a list and get all the even numbers [filter]
#2.Double each element of the list          [map]
#3.Sum the elements of the list            [reduce]

sample_list=[2,3,4,5,6,9,32,46,100]

evens= list(filter(lambda x: x%2==0,sample_list))
print("Filter operation to get below even list:")
print(evens)

double_evens= list(map(lambda x: x*2, evens))
print("Map operation doubles each of the even numbers in the list as below")
print(double_evens)

sum_evens= reduce(lambda x,y: x+y, double_evens)
print("Reduce operation sums each of the doubled even element and produce the result below:")
print(sum_evens)