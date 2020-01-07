# Below problem is to divide an input string str into k divisions
# and output unique characters from each division in existing order as inside the string
# For ex: SATAVISHA, 5 Output:
# SATV
# ISHA

from collections import OrderedDict
def merge_the_tools (str, k):
    ln= len(str)
    unique= set()
    for i in range(0, ln, k):
        sub_str=str[i:i+k]
        print(''.join(OrderedDict.fromkeys(sub_str).keys()))


if __name__=="__main__":
    str, k= input("Enter string : "), int(input("Enter no. of divisions :"))
    merge_the_tools(str, k)