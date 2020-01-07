# There is an array of length n
# There is a
from itertools import groupby
def calculate_happiness(n,m,arr, a,b):
    pos=0
    neg=0
    for i in arr:
        if i in a:
            pos=pos +1
        if i in b:
            neg=neg +1
    print(pos-neg)

if __name__=="__main__":
    n, m= input().split(" ")
    arr= input().split(" ")
    a= set(input().split(" "))
    b= set(input().split(" "))
    calculate_happiness(int(n), int(m), arr, a,b)
