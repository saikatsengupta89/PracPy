# When python runs a code, before even running the code it sets various variables. The __name__ variable
#is one such variable. When python runs a python file directly, it sets the name of the __name__ variable to the
#__main__. Whenever we import a module, it will set the name of the __name__ variable to the name of the file.
#
from calc_module import *

print ("This module is importing calc, but it's not printing the module name as it's the main function and not calc")
print ("Hello ", __name__)