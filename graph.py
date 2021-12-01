import numpy as np
import vertex, random
edge_weight_range = 20

class Graph:
    def __init__(self, graph_verts_num):
        self.vertices = {}
        self.man_adj_mat = np.zeros(shape=(graph_verts_num, graph_verts_num))
        self.adjacency_matrix = np.zeros(shape=(graph_verts_num, graph_verts_num))
    
    def add_vertex(self, vert):
        if isinstance(vert, vertex.Vertex):
            self.vertices[vert.name] = vert.neighbors

    def add_vertices(self, vertices):
        for vert in vertices:
            if isinstance(vert, vertex.Vertex):
                self.vertices[vert.name] = vert.neighbors
            
    def add_edge(self, start_vert, end_vert, i_idx, j_idx):
        self.adjacency_matrix[i_idx-1,j_idx-1] = self.adjacency_matrix[j_idx-1,i_idx-1] = random.randint(1, edge_weight_range)
        if isinstance(start_vert, vertex.Vertex) and isinstance(end_vert, vertex.Vertex):
            start_vert.add_neighbor(end_vert)
            if isinstance(start_vert, vertex.Vertex) and isinstance(end_vert, vertex.Vertex):
                self.vertices[start_vert.name] = start_vert.neighbors
                self.vertices[end_vert.name] = end_vert.neighbors
    
    def adjacencyList(self):
        if len(self.vertices) >= 1: return [(self.vertices[key]) for key in self.vertices.keys()]  
        else: return dict()

    def add_edge_mst(self, start_vert, end_vert):
        if isinstance(start_vert, vertex.Vertex) and isinstance(end_vert, vertex.Vertex):
            start_vert.add_neighbor(end_vert)
            if isinstance(start_vert, vertex.Vertex) and isinstance(end_vert, vertex.Vertex):
                self.vertices[start_vert.name] = start_vert.neighbors
                self.vertices[end_vert.name] = end_vert.neighbors