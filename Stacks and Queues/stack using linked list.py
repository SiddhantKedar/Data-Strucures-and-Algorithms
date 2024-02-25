
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
        
    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        
    def pop(self):
        if self.top == None:
            print("Stack is empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if self.bottom == None:
                self.bottom = None
                
    def print_stack(self):
        if self.top == None:
            print("Stack is empty")
        else:
            pointer = self.top
            while pointer != None:
                print(pointer.data)
                pointer = pointer.next
        
        
my_stack = Stack()

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
