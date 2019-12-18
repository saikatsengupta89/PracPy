from array import *
# below code to construct a list or an array depending on conditions
lst=[]
arr=array('d',[])

def print_array(arr):
        print("Printing the array constructed")
        for i in range(len(arr)):
            print(arr[i], end=" ")

def construct_array (typ, arr_lst_flag, code):
    if(arr_lst_flag=="List"):
        lst_length= int(input("Enter length of the array"))
        for i in range(lst_length):
            element= str(input("Enter element "+str(i+1)+ " :"))
            lst.append(element)
        print_array(lst)

    elif(arr_lst_flag== "Array" and code == 'i'):
        arr= array('i',[])
        arr_length= int(input("Enter length of the array"))
        for i in range(arr_length):
            element= int(input("Enter element "+str(i+1)+ " :"))
            arr.append(element)
        print_array(arr)

    elif(arr_lst_flag == "Array" and code == 'd'):
        arr = array('d', [])
        arr_length = int(input("Enter length of the array"))
        for i in range(arr_length):
            element = float(input("Enter element " + str(i + 1) + " :"))
            arr.append(element)
        print_array(arr)

#take input length, input type and input array and print
typ= str(input("Enter the type of data you would like to insert (string/int/double)"))
if(typ=="String" or typ=="string"):
    construct_array(typ,"List", 's')
elif(typ=="int"):
    construct_array(typ,"Array",'i')
elif(typ=="double"):
    construct_array(typ,"Array",'d')
else:
    print("Not valid entry")