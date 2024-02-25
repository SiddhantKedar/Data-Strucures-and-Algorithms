# 10 ---> 5 --> 16


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def insert(self,index,value):
        new_node = Node(value)
        i = 0
        temp = self.head
        
        if index >= self.length:
            self.append(value)
            return
        if index == 0:
            self.prepend(value)
            return
        
        while i < self.length:
            if i == index - 1:
                temp.next = new_node
                new_node.next = temp.next
                self.length += 1
                break
            temp = temp.next
            i += 1
            
    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()
        print("Length = " + str(self.length))
        
    def remove(self, index):
        temp = self.head
        i = 0
        
        if index >= self.length:
            print("Entered wrong index")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        while i < self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            
        i += 1
        temp = temp.next
        
    
l = LinkedList()
l.append(5)
l.prepend(7)
l.insert(3,20)
l.remove(2)
l.printl()
