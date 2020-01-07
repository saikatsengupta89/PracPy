def organizingContainers (container):
    cont_vol=list()
    type_vol=list()
    l= len(container[0])
    for i in range(l):
        cont_vol.append(sum(container[i]))
        col_sum = 0
        for j in range(l):
            col_sum= col_sum + container[j][i]
        type_vol.append(col_sum)

    cont_vol= sorted(cont_vol)
    type_vol= sorted(type_vol)

    if(cont_vol==type_vol):
        return "Possible"
    else:
        return "Not Possible"

if __name__=="__main__":
    n= int(input("Enter total no. of cases"))
    container=list()
    for i in range(n):
        k= int(input("Enter no. of containers and balls type"))
        for i in range(k):
            m= list(map(int, input().split(" ")))
            container.append(m)
        result=organizingContainers(container)
        print(result)