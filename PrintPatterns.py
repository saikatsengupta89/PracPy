#printing the pattern in the below format
####
####
####
####

for i in range(4):
    for j in range(4):
        print (str('#')+" ", end="")
    print()

#printing the pattern in the below format
#
##
###
####

for i in range(5):
    for j in range(i):
        print (str('#')+" ", end="")
    print()
print()
#printing the pattern in the below format
####
###
##
#

for i in range(4):
    for j in range(4-i):
        print (str('#')+" ", end="")
    print()