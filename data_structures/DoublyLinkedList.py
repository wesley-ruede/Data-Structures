"""
Linked Lists -------

Node -------
A class which holds data and a reference/pointer/node to the next data
Used when the allocation of memory cannot be a continuous block of memory
This sctructure is known as a pointer in other languages such as C and C++

Node
   x-----xx-----x
<--|<-*  ||  *->|-->
   x-----||-----x
<--|     ||  4  |-->
   x-----xx-----x
    prev,   next
    None,   data

Doubly Linked List -------
# contains a link element to first, is first in last out (FILO)
# each link contains a data field and two properties called prev and next
# each link is connected using it next and previous to the respective links
# the last link has a null/None pointer to mark the end of the list

Methods: traverse, insert, append

x-----xx-----x   X-----xx-----x   x-----xx-----x
|<-*  ||  *->|<--|<-*  ||  *->|<--|<-*  ||  *->|
x-----xx-----x   x-----xx-----x   x-----||-----x
x-----xx-----x   x-----xx-----x   x-----||-----x
|     ||  5  |-->|     ||  6  |-->|     ||  7  |--> ect.
x-----xx-----x   x-----xx-----x   x-----xx-----x
 prev,  next      prev,  next      prev,  next  
 None,  data      None,  data      None,  data  


"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:

    def __init__(self):
        self.head = None

# add an element to the front
    def push(self,NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

# add an element to the end    
    def append(self,NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.hed = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode = last
        return

    def insert(self,prev_node,NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.previous = NewNode

# print the linked list
    def listprint(self,node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

# create a Dll and add values to it
dll = DLinkedList()
dll.push(58)
dll.push(9)
dll.push(124)
# print the elements
dll.listprint(dll.head.next.prev)
dll.listprint(dll.head)
dll.listprint(dll.head.next)
# insert at a location
dll.insert(dll.head.next, 25)
dll.listprint(dll.head)
# append a value
dll.append(45)
dll.listprint(dll.head)
