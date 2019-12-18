from time import sleep
from threading import *
#to make both the threads run paralley to produce hi and hello simultaneously, you need to provide LAG between execution
class Hello (Thread):
    def run(self):
        for i in range(5):
            print ("Hello")
            sleep(1)

class Hi (Thread):
    def run(self):
        for j in range(5):
            print ("Hi")
            sleep(1)

t1= Hello()
t2= Hi()

#the below start commands will start the two threads t1 and t2 simultaneously
#run method is defined as these two methods are already defined inside threading.
#when start() method is called, run() method is automatically called
t1.start()
sleep(0.5)
t2.start()

#the below commands will make the main thread to wait for child threads t1 and t2 to complete
#finally after all the operations are completed, the main thread will print 'Bye' and complete execution.
t1.join()
t2.join()
print("Bye")