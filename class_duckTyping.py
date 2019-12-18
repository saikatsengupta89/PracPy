class PyCharm:
    def execute(self):
        print ("Compiling")
        print ("Running")

class Mycharm:
    def execute(self):
        print ("Spell Check")
        print ("Convention Check")
        print ("Compiling")
        print ("Running")

class Laptop:
    def code (self, ide):
        ide.execute()

ide= PyCharm()

#passing ide via laptop instance
lap1= Laptop()
lap1.code(ide)

#now in future if you want to hchange ide from Pycharm to MyCharm, its completely doable as long as both
#the editors are having the same execute function.
#you can always change as below
print()
print("In future the IDE changes from PyCharm to Mycharm")

ide=Mycharm()
lap1.code(ide)