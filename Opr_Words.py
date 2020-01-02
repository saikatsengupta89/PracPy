from collections import Counter
def count_distinct(lst):
    counter=0
    unique=set()
    for i in lst:
        unique.add(i)
    print(len(unique))

def count_appearance(lst):
    c= Counter(lst)
    for k, v in c.items():
        print(v, end=" ")


if __name__ =="__main__":
    lst=[]
    n= int(input("Enter the total number of words you want to enter"))
    for i in range(n):
        word= input("Enter word "+ str(i+1)+ ":")
        lst.insert(i, word)
    count_distinct(lst)
    count_appearance(lst)