class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}
        
    def add_vertex(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            self.number_of_nodes += 1
            return
        
    def add_edge(self, node1, node2):
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return
        return "Edge already exists"
    
    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')
            
my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.show_connections()

print(my_graph.adjacency_list)
#{1: [2, 3], 2: [1, 3], 3: [1, 2]}

print(my_graph.number_of_nodes)
#3
