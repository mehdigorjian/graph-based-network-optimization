import time, random, graph, vertex
probability = 20
average_vertex_degree = 6
def graph1(verts_num):
	V, verts_list = [], []
	for i in range(verts_num + 1): verts_list.append(vertex.Vertex(i))
	for i in range(verts_num + 1): V.append(i)
	edge_count = 0
	g = graph.Graph(verts_num)
	g.add_vertices(V[1:])
	for i in range(1, verts_num):
		g.add_edge(verts_list[i], verts_list[i+1], i, i+1)
		edge_count = edge_count + 1	

	g.add_edge(verts_list[verts_num], verts_list[1], verts_num, 1)
	edge_count = edge_count + 1
	avg_verts_deg = average_vertex_degree
	edges_num = verts_num * avg_verts_deg/2
	start = time.time()
	def non_adj_verts(index):
		non_adj_lst = []
		if index != verts_num and index !=1: non_adj_lst = V[index+2:]
		if index == 1: non_adj_lst = V[index+2:-1]
		return non_adj_lst
	mix, non_adj_verts_list = [], []
	non_adj_verts_list.append([])
	for i in range(verts_num): non_adj_verts_list.append(non_adj_verts(i+1))
	for i in range(1,len(non_adj_verts_list)):
		for j in range(len(non_adj_verts_list[i])):
			mix.append([i, non_adj_verts_list[i][j]])
	e_rand =  random.sample(mix, edges_num - verts_num)
	for i in range(len(e_rand)):
		g.add_edge(verts_list[e_rand[i][0]], verts_list[e_rand[i][1]], e_rand[i][0], e_rand[i][1])
		edge_count = edge_count + 1

	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix
	print('[result] Number of Edges in Graph G1: ' + str(edge_count))
	print('[result] Total Time for creating Graph G1: ' + str(time.time() - start) + ' s')
	return [adj_list, adj_mat]

def graph2(verts_num):
	V, verts_list = [], []
	for i in range(verts_num+1): verts_list.append(vertex.Vertex(i))
	for i in range(verts_num+1): V.append(i)
	edge_count = 0
	g = graph.Graph(verts_num)
	g.add_vertices(V[1:])
	for i in range(1,verts_num):
		g.add_edge(verts_list[i], verts_list[i+1], i, i+1)
		edge_count = edge_count + 1	
	g.add_edge(verts_list[verts_num], verts_list[1], verts_num, 1)
	edge_count = edge_count + 1
	start = time.time()
	for i in range(verts_num):
		for j in range(i+2, verts_num):
			probab = random.randint(0, 100)
			if(i == 0 and j == verts_num - 1): continue
			if(probab <= probability):
				g.add_edge(verts_list[i+1], verts_list[j+1], i+1, j+1)
				edge_count = edge_count + 1
				
	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix
	print('[result] Number of Edges in Graph G2: ' + str(edge_count))
	print('[result] Total Time for creating Graph G2: ' + str(time.time() - start) + ' s')
	return [adj_list, adj_mat]