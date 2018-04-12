import random
import copy

#Ring Initialization
def makeRing(n,k):

    state_count = n
    ring_network = {}

    for i in range(0,state_count):

        if i==0:
            ring_network[i] = [i,random.randint(0,k),-1]

        elif i==state_count-1:
            ring_network[i] = [i,random.randint(0,k),1]

        else:
            ring_network[i] = [i,random.randint(0,k),0]

    return ring_network

def printRingState(ring_network):

    for i in range(0,len(ring_network)):
        print(ring_network[i])

    print("\n")

#Main Function
states = 3
processors = 4
ring_network = makeRing(processors,states)

print("State of the initial ring is:\n")
printRingState(ring_network)

flag = True
counter = 1

while flag==True:

    temp = copy.deepcopy(ring_network)

    print(temp)
    print("\n")

    for i in range(0,processors):

        if ring_network[i][2]==-1:
            
            right = (i+1)%processors

            if ring_network[i+1][1]%3==ring_network[right][1]:

                left = (i-1)%processors
                ring_network[i][1] = ring_network[left][1]%3

        elif ring_network[i][2]==1:
            
            right = (i+1)%processors
            left = (i-1)%processors

            if ring_network[right][1]==ring_network[left][1] and ring_network[left+1][1]%3!=ring_network[i][1]:

                ring_network[i][1] = ring_network[left+1][1]%3

        else:

            right = (i+1)%processors
            left = (i-1)%processors

            if ring_network[i+1][1]%3==ring_network[left][1]:

                ring_network[i][1] = ring_network[left][1]

            if ring_network[i+1][1]%3==ring_network[right][1]:

                ring_network[i][1] = ring_network[right][1]

        print(str(counter) + ". State of the ring after " + str(i) + " processor:\n")
        printRingState(ring_network)
    
    counter += 1

    if cmp(temp,ring_network)==0:
        
        flag = False
        break
