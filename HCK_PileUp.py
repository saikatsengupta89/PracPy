"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if cubei is on top of cubej then sideLengthj > sideLengthi.
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
"""
from collections import deque
def pile_possibility (n, lst):
    even_flag=0
    possible_flag=1
    min_pop=min(int(lst[0]), int(lst[n-1]))
    if n % 2 == 0:
        even_flag = 1
    else:
        even_flag = 0
    if even_flag == 1:
        while (len(lst) >2):
            popl = int(lst.popleft())
            popr = int(lst.pop())
            if (popl > min_pop or popr > min_pop):
                possible_flag=0
                break
            else:
                min_pop= min(popl, popr)
            popr= int(lst.pop())
            popl= int(lst.popleft())
            if(popr==popl):
                possible_flag = 0
            else:
                possible_flag = 1
    else:
        while (len(lst) > 1):
            popl = int(lst.popleft())
            popr = int(lst.pop())
            if (popl > min_pop or popr > min_pop):
                possible_flag=0
                break
            else:
                min_pop= min(popl, popr)
        popr= int(lst.pop())
        if (popr > min_pop):
            possible_flag=0

    if possible_flag==0:
        return "No"
    else:
        return "Yes"

if __name__== "__main__":
    inp= int(input("Enter no. of inputs"))
    output=list()
    for i in range(inp):
        n= int(input("Enter no. of cubes"))
        k= str(input("Enter cube side lengths"))
        d= deque(k.split(" "))
        output.append(pile_possibility(n, d))

    for i in output:
        print(i)