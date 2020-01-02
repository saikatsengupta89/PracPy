lst1= [1,2,3,4,6.4,'Str']
lst2= [3,4,6,'I','You']
print(lst1[0])
lst1[0]='Changed'
print(lst1)
lst1.insert(6,'Ele1')
lst1.insert(7,'Ele2')
print(lst1)
lst1.pop()
print(lst1)
lst1.pop(2)
print(lst1)
lst_rev= lst1.reverse()
print(lst_rev)