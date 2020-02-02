# procedural stack

import time

stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


def timer():
    timeleft = int(input("Enter the time in seconds: "))
    while timeleft > 0:
        count = print(timeleft)
        time.sleep(1)
        timeleft = timeleft - 1
        stack.append(timeleft)

# object oriented stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def timer(self):
        timeleft = int(input("Enter the time in seconds: "))
        while timeleft > 0:
            count = print(timeleft)
            time.sleep(1)
            timeleft = timeleft - 1
            self.stack.append(timeleft)
        pass
    
Stack = Stack()
Stack.push(timer())
Stack.stack.append(push)

import time

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val
    pass

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()
little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop(), 'the stack is working')


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self,val):
        self.__sum += val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    pass

stack = AddingStack()
for i in range(5):
    stack.push(i)
print('The sum of the values on the stack are:', stack.getSum())
for i in range(5):
    time.sleep(1)
    print('the values on the stack are: \n', stack.pop())

