from collections import deque
def operations(opr):
    if opr[0]=="append":
        d.append(opr[1])
    elif opr[0]=="appendleft":
        d.appendleft(opr[1])
    elif opr[0]=="pop":
        d.pop()
    elif opr[0]=="popleft":
        d.popleft()
    else:
        pass


if __name__ == "__main__":
    n= int(input("Enter number of operations : "))
    d= deque()
    for i in range(n):
        inp= str(input("Enter Operation separated by values "))
        k= inp.split(" ")
        operations(k)

    for i in d:
        print(i, end=" ")