'''
Node -------
A class which holds data and a reference/pointer/node to the next data
Used when the allocation of memory cannot be a continuous block of memory
This sctructure is known as a pointer in other languages such as C and C++

Node
x-----xx-----x
|  5  ||<-*->|
x-----xx-----x
data  , next
'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

# usage 
element1 = Node(0)
element2 = Node(1)
element3 = Node(2)
element4 = Node(3)
# nextval used to point to the next data point
element1.next = element2
element2.next = element4
element4.next = element3

#traverse the nodes
thisval = element1
while thisval:
    print(thisval.dataval)
    thisval = thisval.next
