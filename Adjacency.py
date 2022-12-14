class Vertex:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

class Matrix:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {} 
    
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex.__str__(), to_vertex.__str__())] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
    
    def add_undirected_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.add_directed_edge(from_vertex, to_vertex, weight)
        self.add_directed_edge(to_vertex, from_vertex, weight)