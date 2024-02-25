class Stack:
    def __init__(self):
        self.array = []
        
    def peek(self):
        return self.array[len(self.array)-1]
        
    def push(self, data):
        self.array.append(data)
        return 
        
    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
        else:
            print("Stack is Empty")
            
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return

my_stack = Stack()    
my_stack.push("1")
my_stack.push("2")
my_stack.push("3")
my_stack.push("4")
my_stack.print_stack()

