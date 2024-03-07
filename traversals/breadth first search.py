class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0
        
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.no_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.no_of_nodes += 1
            return
            
    def search(self, data):
        if self.root == None:
            return "Tree is empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right
                    
    def remove(self,data):
        if self.root == None:
            return "Tree is empty"
        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else: #match found
                #Node has only left child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parrent_node.right = current_node.left
                            return
                #Node has only right child
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parrent_node.right = current_node.right
                            return
                #Node has no left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return
                
                #Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                    return
        return "Not Found"
                
    def BFS(self):
        current_node = self.root
        if current_node is None:
            return "Tree is empty"
        else:
            bfs_result = []
            queue = []
            queue.append(current_node)
            while len(queue) > 0:
                current_node = queue.pop(0)
                bfs_result.append(current_node.data)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return bfs_result
        
    def BFS_recursive(self,queue, bfs_list):
        if self.root == None:
            return "Tree is empty"
        if len(queue) == 0:
            return bfs_list
        current_node = queue.pop(0)
        bfs_list.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.BFS_recursive(queue, bfs_list)
        
        
tree = BinarySearchTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(13)
tree.insert(65)
tree.insert(0)
tree.insert(10)
print(tree.search(13))
print("Current Length:",tree.no_of_nodes)
'''
            5
        3       7
    1              13        
0           10           65    
'''

print(tree.BFS())  
print(tree.BFS_recursive([tree.root], []))
'''
[5, 3, 7, 1, 13, 0, 10, 65]
'''
