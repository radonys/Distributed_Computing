#Imports
import random
import sys
from threading import Thread

x = {} #Process Dictionary

#Class Definition
class Channel:
    
    def __init__(self, destinationNode, processId, currentRound):
	    
        self.pid = processId
        self.round = currentRound
        self.destination = destinationNode

    def passMessage(self, message, side, flag=0):
        
        print "Process ", self.pid, ": send ", message, " to ", " Process", self.destination.pid
        self.destination.receive(message, flag, self.pid, self.round)

class Process:

    def __init__(self, pid, value, flagl=0, flagr=0):

        self.left_value = value
        self.right_value = value
        self.left_flag = flagl
        self.right_flag = flagr
        self.area = 0
        self.round = 0
        self.pid = pid
        self.right_node = None
        self.left_node = None
        self.tempL_value = None
        self.tempL_flag = 0
        self.tempR_value = None
        self.tempR_flag = 0

        if flagl==1:
            self.right_value = sys.maxint
        
        if flagr==1:
            self.left_value = -sys.maxint

    def send(self):
        
        if self.right_node != None:
            
            ch = Channel(self.right_node, self.pid, self.round)
            ch.passMessage(self.right_value, self.right_flag)
				
        if self.left_node != None:
            
            ch = Channel(self.left_node, self.pid, self.round)
            ch.passMessage(self.left_value, self.left_flag)

    def receive(self, message, flag, processId, currentRound):
        		
        print "Process ", processId, ": Receive ", message, " to ", " Process", self.pid

        if processId > self.pid:
            if message < self.right_value:
                    
                self.tempR_value = message
                self.tempR_flag = flag

        else:
            if message > self.left_value:
                self.tempL_value = message
                self.tempL_flag = flag
    
    def local(self):

        self.round = self.round + 1

        if self.tempR_value != None:

            self.right_value = self.tempR_value
            self.right_flag = self.tempR_flag
            self.tempR_value = None

        if self.tempL_value != None:
    
            self.left_value = self.tempL_value
            self.left_flag = self.tempL_flag
            self.tempL_value = None

        if self.left_value>self.right_value:
                
            temp = self.left_value
            self.left_value = self.right_value
            self.right_value = temp

            temp = self.left_flag
            self.left_flag = self.right_flag
            self.right_flag = temp

#Code
def main(n):
    
    print "Number of processes: ", n

    for i in range(1,n+1):
        
        if i==1:
            x[i] = Process(i,random.randint(1,n),flagr=1)
        
        elif i==n:
            x[i] = Process(i,random.randint(1,n),flagl=1)

        else:
            x[i] = Process(i,random.randint(1,n))
    
    print "Initial State of Processes\n"
    
    for i in range(1,n+1):
		print "Process ", x[i].pid, " : ", x[i].left_value, "|", x[i].right_value

    for i in range(1,n+1):
        
        if i!=n:
            x[i].right_node = x[i+1]
            x[i+1].left_node = x[i]

    print "\n"

    for j in range(1,n):
        
        for i in range(1,n+1):
            
            t = Thread(target=x[i].send())
            t.start()
        
        print "\nRound ", j, " over \n"
            
        for i in range(1,n+1):
            
            x[i].local()
            print "Process ", x[i].pid, ": ", x[i].left_value, '|', x[i].right_value
		
        print "\n"

    print "Final State of Processes\n\n"
	
    for i in range(1,n+1):
            
        print "Process ", x[i].pid, " : ", x[i].left_value, "|", x[i].right_value

    print "\n"

if __name__ == "__main__":
	main(int(sys.argv[1]))