class Computer:
    ## __init__ is called everytime we crete an instance of the class.
    ## for every object it will get called once.
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print ("Config is : ", self.cpu, self.ram)


com1= Computer ("i7", "512GB")
com2= Computer ("i9", "1TB")

com1.config()
com2.config()

