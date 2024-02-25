class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek():
        return self.first.data
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.last == None:
            self.last = new_node
            self.first = self.last
            self.length += 1
            return 
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return
    
    def dequeue(self):
        if self.last == None:
            print("Queue is empty")
            return
        if self.last == self.first:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return
        
        
    def print_queue(self):
        if self.length == 0:
            print("Queue is empty")
            return
        else:
            pointer = self.first
            while pointer != None:
                if pointer.next == None:
                    print(pointer.data)
                else:
                    print(f"{pointer.data} <--",end=" ")
                pointer = pointer.next
            return

my_queue = Queue()
my_queue.enqueue("This")
my_queue.enqueue("is")
my_queue.enqueue("a")
my_queue.enqueue("Queue")
my_queue.print_queue()
#This  <<--  is  <<--  a  <<--  Queue
            
        
