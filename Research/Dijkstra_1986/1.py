import random
import copy

def makeString(n):

    state_count = n
    ring_network = {}

    for i in range(0,state_count):

        if i==0:
            ring_network[i] = [i,random.randint(0,3)%3,-1]

        elif i==state_count-1:
            ring_network[i] = [i,random.randint(0,3)%3,1]

        else:
            ring_network[i] = [i,random.randint(0,3)%3,0]

    return ring_network

'''def printStringState(ring_network):

    string = ''

    for i in range(0,len(ring_network)):
        
        if ring_network[i][2]==-1:
            string += 'B'

        if ring_network[i][2]==1:
            string += 'T'

        else:
            string += 'S'

    print(string)'''

def printRingState(ring_network):

    for i in range(0,len(ring_network)):
        print(ring_network[i])

    print("\n")

#Main Function
max_length = random.randint(2,3)
state_string = makeString(max_length)
#printStringState(state_string)

flag = True
counter = 1

while flag==True:

    temp = copy.deepcopy(state_string)

    print(temp)
    print("\n")

    for i in range(0,len(state_string)):

        if state_string[i][2] == -1:
            
            right = (i+1)%max_length

            if state_string[i][1] == state_string[right][1]:

                state_string[i][1] += 1
                state_string[i][1] = state_string[i][1]%3

        if state_string[i][2] == 0:

            right = (i+1)%max_length
            left = (i-1)%max_length

            if state_string[left][1] == state_string[i][1] + 1 or state_string[i][1] + 1 == state_string[right][1]:

                state_string[i][1] += 1
                state_string[i][1] = state_string[i][1]%3

        else:

            left = (i-1)%max_length

            if state_string[left][1] == state_string[0][1] and state_string[i][1] != state_string[0][1] + 1:

                state_string[i][1] = state_string[0][1] + 1
                state_string[i][1] = state_string[i][1]%3

        print(str(counter) + ". State of the string after " + str(i) + " processor:\n")
        printRingState(state_string)

    counter += 1

    if cmp(temp,state_string)==0:
        
        flag = False
        break

     
