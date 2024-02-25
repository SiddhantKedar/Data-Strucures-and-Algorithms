#adding a previous node

class Node():
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
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
            new_node.previous = self.tail
            self.tail = new_node
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1
    
    def insert(self,index,value):
        new_node = Node(value)
        i = 0
        temp = self.head
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        else:
            leader = self.traversetoindex(index-1)
            holder = leader.next
            new_node.next = holder
            new_node.previous = leader
            holder.previous = new_node
            self.length += 1
            
    def traversetoindex(self,index):
        curr_node = self.head
        i = 0
        while i!= index:
            curr_node = curr_node.next
            i+=1
        return curr_node
            
    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()
        print("Length = " + str(self.length))
        
    def remove(self, index):
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        leader = self.traversetoindex(index-1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.previous = leader
        self.length -= 1

    
l = DoublyLinkedList()
l.append(5)
l.append(10)
l.append(8)
l.prepend(7)
l.insert(1, 99)
l.remove(2)
l.printl()

