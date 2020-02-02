def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch,t,[]])
    else:
        root.insert(1, [newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch,t,[]])
    else:
        root.insert(2, [newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[1]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(r,9)
print(r)
insertLeft(r,22)
print(r)
print(getRightChild(getRightChild(r)))

''' OOP Binary Search Tree '''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class BST:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None
        
    def contains(self, node):
        if self.left == None and self.right == None:
            return node.value == self.node.value
        elif self.left != None and node.key < self.node.key:
            return self.left.contains(node)  
        elif self.right != None and node.key > self.node.key:
            return self.right.contains(node)
            
    def add(self, node):
        if node.key == self.node.key:
            self.node = node
        elif node.key < self.node.key:
            if self.left == None:
                self.left = BST(node)
            else:
                self.left.add(node)
        else:
            if self.right == None:
                self.right = BST(node)
            else:
                self.right.add(node)

