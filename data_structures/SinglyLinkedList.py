"""
Linked Lists -------

Node ----------
# A sequence of data elements connected by links.
# Data elements are connected with pointers called Nodes
# Nodes require literal data and a reference to the next object

Node
x-----x
|<-*->|
x-----x
 data

Singly Linked List -------
# SLl can only link any two Nodes of data in a forward fashion
# SLl can only be traversed forward
# Methods: traverse, insert, and remove, need update

SLinkedList
x-----xx-----x   x-----xx-----x   x-----xx-----x
|  5  ||  *->|-->|  6  ||  *->|-->|  7  |   *->|--> ect.
x-----xx-----x   x-----xx-----x   x-----xx-----x
data,   root      data,   next     data,   next
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.root = None

    def LlistPrint(self):
        printval = self.root
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def InsertBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.root
        self.root = NewNode

    def InsertEnd(self,newdata):
        NewNode = Node(newdata)
        if self.root is not None:
            self.root = NewNode
            return
        
        laste = self.root
        while(laste.next):
            laste = laste.next
        laste.next = NewNode

    def InsertAfter(self,node,newdata):
        if node is None:
            print("the given node not available")
            return
# my abstraction skills really didn't work that well
        NewNode = Node(newdata)
        NewNode.next = node.next
        node.next = NewNode

    def RemoveNode(self,Removekey):

        HeadVal = self.root
        
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.root = HeadVal.next
                HeadVal = None
                return
        while(HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None



# create nodes 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
# instantiate singly linked list and add the root
sll = SLinkedList()
sll.root = Node("root")
# add nodes to singly linked list
sll.root.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
# print the singly linked list
sll.LlistPrint()
#insert at beginning of the list
sll.InsertBeginning(10)
sll.LlistPrint()
# insert after
sll.InsertAfter(sll.root.next.next.next.next.next,789)
sll.InsertAfter(sll.root.next.next,12)
sll.InsertAfter(sll.root.next,50)
#insert directly after the root
sll.InsertAfter(sll.root,25)
sll.LlistPrint()
# delete a node
sll.RemoveNode(2)
sll.LlistPrint()

"""
Traversal method ---

Get the root, loop through the SLL till there are no remaining nodes, display
the data, and move from the root node until next is None e.g. no more nodes.

Insert Methods ---

InsertBeginning-> A Node is passed as data and a pointer. Point NewNode to the
to the root as its location and set the Node object as the root value.

InsertEnd-> if there is no root set the newdata as the root an index to move
to the end of the list and then place the value at the end of the list

Remove Method ---

RemoveNode-> In case the roots data value is exactly equal to the remove_key parameter
set the root as next which is None and return that the Sll is now empty.
While waiting for the data value to match the remove_key, step through the list.
If the value is not found return None, if the value is found then set node
prior to the remove_key then point to the next pointer of the next node to be deleted
Side Note: printing the value as a variable will give you None.
"""

" possible stuff "
##insert_at_six = sll.insertAfter(sll.root.next.next.next.next.next,789)
##sll.listPrint()
##exec(insert_at_six(12))
