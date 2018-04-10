#!/usr/bin/python3 

#imported modules

#This is imported to assign random value to process value
from random import randrange
#It's for creating channel between two nodes
import sys
from threading import Thread

class Channel:
	def __init__(self, destinationNode, processId, currentRound):
		self.processId = processId
		self.currentRound = currentRound
		self.destinationNode = destinationNode

	def passMessage(self, message):
		#print("Process ", self.processId, ": send ", message, " to ", " Process", self.destinationNode.processId)
		self.destinationNode.recieveMessage(message, self.processId, self.currentRound)

class Process:
	def __init__(self, processId):
		self.leftNode = None
		self.rightNode = None
		self.currentRound = 0
		self.value = randrange(1,100)
		self.processId = processId
		self.temp = None

	#Every node will send a message but the direction depends upon round and process id
	def sendMessage(self):
		
		if self.checkEvenOdd(self.currentRound) == self.checkEvenOdd(self.processId):
			#Send to the right node
			if self.rightNode != None:
				ch = Channel(self.rightNode, self.processId, self.currentRound)
				ch.passMessage(self.value)
				
			#Send roundCount to left node
			if self.leftNode != None:
				ch = Channel(self.leftNode, self.processId, self.currentRound)
				ch.passMessage("roundCount")

		else:
			#Send to the left node
			if self.leftNode != None:
				ch = Channel(self.leftNode, self.processId, self.currentRound)
				ch.passMessage(self.value)
				self.swap()
			#Send roundCount to right node
			if self.rightNode != None:
				ch = Channel(self.rightNode, self.processId, self.currentRound)
				ch.passMessage("roundCount")


	def recieveMessage(self, message, processId, currentRound):
		
		#print("Process ", processId, ": Receive ", message, " to ", " Process", self.processId)
		#Does some local processing e.g. swapping, updating current round
		self.localProcessing(currentRound) 

		if message != "roundCount":
			if processId > self.processId:
				if message < self.value:
					#store in temp 
					self.temp = message
					self.swap()
			else:
				if message > self.value:
					#store in temp
					self.temp = message

		self.incrementRound() 	#for leftmost node
	


	#It's invoked when a round finishes
	def localProcessing(self, currentRound):
		if currentRound > self.currentRound:
			#update the currentRound
			self.currentRound = currentRound
			#Swap the temp variable with value object variable


	def swap(self):
		if self.temp != None:
			self.value = self.temp
			self.temp = None


	#Increase the counter by 1
	#Only invoked for the leftmost node	
	def incrementRound(self):
		if self.leftNode == None:
			self.currentRound += 1


	#Returns even or odd as string 
	def checkEvenOdd(self, inputValue):
		if inputValue % 2 == 0:
			return "even"
		else:
			return "odd"



def main(noOfProcesses):
	processes = []
	i = 0
	while i < noOfProcesses:
		obj = Process(i)
		processes += [obj]
		i += 1

	print("\nInitial State of Processes\n\n")
	for i in processes:
		print("Process ", i.processId, " : ", i.value)

	i = 0
	while i < noOfProcesses - 1:
		processes[i].rightNode = processes[i+1]
		processes[i+1].leftNode = processes[i]
		i += 1

	print("\n")

	i = 0
	while i < noOfProcesses:
		for obj in processes:
			t = Thread(target=obj.sendMessage())
			t.start()
		#print("\n\n Round ", i, " over \n\n")
		if noOfProcesses<=10 and (noOfProcesses/2)%(i+1)==0:
			for obj in processes:
				print("Process ", obj.processId, ": ", obj.value)
			print("\n\n")

		if noOfProcesses>10 and (noOfProcesses/5)%(i+1)==0:
			for obj in processes:
				print("Process ", obj.processId, ": ", obj.value)
			print("\n\n")

		i += 1

	print("Final State of Processes\n\n")
	for i in processes:
		print("Process ", i.processId, " : ", i.value)
		

if __name__ == "__main__":
	main(int(sys.argv[1]))
	