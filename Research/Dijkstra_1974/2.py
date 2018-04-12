import random
import copy

#Ring Initialization
def makeRing(n):

    state_count = n
    ring_network = {}

    for i in range(0,state_count):

        if i==0:
            ring_network[i] = [i,random.choice([True, False]),True,-1]

        elif i==state_count-1:
            ring_network[i] = [i,random.choice([True, False]),False,1]

        else:
            ring_network[i] = [i,random.choice([True, False]),random.choice([True, False]),0]

    return ring_network

def printRingState(ring_network):

    for i in range(0,len(ring_network)):
        print(ring_network[i])

    print("\n")

#Main Function
processors = 4
ring_network = makeRing(processors)

print("State of the initial ring is:\n")
printRingState(ring_network)

flag = True
counter = 1

while flag==True:

    temp = copy.deepcopy(ring_network)
    
    print(temp)
    print("\n")

    for i in range(0,processors):

        if ring_network[i][3]==-1:
            
            right = (i+1)%processors

            if ring_network[i][1]==ring_network[right][1] and (not ring_network[right][2]):

                ring_network[i][1] = not ring_network[i][1]

        elif ring_network[i][2]==1:
        
            left = (i-1)%processors

            if ring_network[i][1]==ring_network[left][1]:

                ring_network[i][1] = not ring_network[i][1]

        else:

            left = (i-1)%processors
            right = (i+1)%processors

            if ring_network[i][1]==ring_network[left][1]:

                ring_network[i][1] = not ring_network[i][1]
                ring_network[i][2] = True

            if ring_network[i][1]==ring_network[right][1] and ring_network[i][2] and (not ring_network[right][2]):

                ring_network[i][2] = False

        print(str(counter) + ". State of the ring after " + str(i) + " processor:\n")
        printRingState(ring_network)
    
    counter += 1

    if cmp(temp,ring_network)==0:
        
        flag = False
        break
