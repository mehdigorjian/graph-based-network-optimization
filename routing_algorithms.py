import numpy as np
import graph, vertex, heap, sys
rightArrow = u'\u2192'.encode("utf-8")
# rightArrow = ' -> '
def path_represent(d, matrix, s, t):
	result = ''
	path = []
	s, t = s-1, t-1
	i = t
	max_bandwidth = sys.maxsize
	path.append(i+1)
	while i != s:
		u = i
		path.append(int(d[i]+1))
		i = d[i]
		v = i
		if(matrix[u][v] < max_bandwidth): max_bandwidth = matrix[u][v]
	for i in range(len(path)): 
		if i != len(path) - 1:
			result = result + str(path[len(path)-i-1]) + ' ' + rightArrow + ' '
		else:
			result = result + str(path[len(path)-i-1])

	return [result, max_bandwidth]

def dijkstra_no_heap(g, s, t):
	adj_list = g[0]
	edge_wts = g[1]
	s, t = s-1, t-1
	verts_num = len(adj_list)
	bw = np.zeros(verts_num)
	dad = np.zeros(verts_num)
	status = []

	for i in range(verts_num): status.append(-1)
	status[s] = 1
	bw[s] = sys.maxsize

	for i in range(len(adj_list[s])):
		w = adj_list[s][i]
		w = w - 1
		status[w] = 0
		bw[w] = edge_wts[s][w]
		dad[w] = s
	
	while status[t] != 1:
		m, max_bw_index = -1, -1
		for i in range(len(status)):
			if status[i] == 0: 
				if bw[i] > m:
					m = bw[i]
					max_bw_index = i
		v = max_bw_index
		status[v] = 1
		for i in range(len(adj_list[v])):
			w =  adj_list[v][i]
			w = w - 1
			if(status[w] == -1):
				status[w] = 0
				bw[w] = min(bw[v], edge_wts[v][w])
				dad[w] = v
			else:
				if status[w] == 0 and bw[w]< min(bw[v], edge_wts[v][w]):
					bw[w] = min(bw[v], edge_wts[v][w])
					dad[w] = v
	max_bandwidth_path = path_represent(dad, edge_wts, s + 1, t + 1)
	print('[Solution 1] Max Bandwidth Path, Dijkstra without Heap: ')
	print('    Max Bandwidth: ' +  str(max_bandwidth_path[1]) + '\n    Max Bandwidth Path:' + str(max_bandwidth_path[0]) + '\n    S-T path: (' + str(s + 1) + ' ' + rightArrow + ' ' + str(t + 1) + ')')

def dijkstra_heap(g, s, t):
	adj_list = g[0]
	edge_wts = g[1]
	s, t = s-1, t-1
	status = []
	verts_num = len(adj_list)
	dad = np.zeros(verts_num)
	bw = np.zeros(verts_num)
	fringeHeap = heap.maxHeap()
	for i in range(verts_num): status.append(-1)
	status[s] = 1
	bw[s] = sys.maxsize
	fringeHeap.Insert(s, bw[s])
	fringeHeap.Delete(1)

	for i in range(len(adj_list[s])):
		w = adj_list[s][i]
		w = w - 1
		status[w] = 0
		bw[w] = edge_wts[s][w]
		fringeHeap.Insert(w, bw[w])
		dad[w]=s
	while status[t] != 1:
		v = fringeHeap.Maximum()
		fringeHeap.Delete(1)
		status[v] = 1

		for i in range(len(adj_list[v])):
			w = adj_list[v][i]
			w = w - 1
			if(status[w] == -1):
				status[w] = 0
				bw[w] = min(bw[v], edge_wts[v][w])
				fringeHeap.Insert(w, bw[w])
				dad[w] = v
			else:
				if status[w] == 0 and bw[w] < min(bw[v], edge_wts[v][w]):
					bw[w] = min(bw[v], edge_wts[v][w])
					fringeHeap.Insert(w, bw[w])
					dad[w] = v
	max_bandwidth_path = path_represent(dad, edge_wts, s + 1, t + 1)
	print('[Solution 2] Max Bandwidth Path: Dijkstra with Heap: ')
	print('    Max Bandwidth: ' + str(max_bandwidth_path[1]) + '\n    Max Bandwidth Path:' + str(max_bandwidth_path[0]) + '\n    S-T path: (' + str(s + 1) + ' ' + rightArrow + ' ' + str(t + 1) + ')')

def kruskal_heapsort(g, s, t):
	lst = g[0]
	matrix = g[1]
	verts_num = len(lst)
	edgesHeap = heap.maxHeap()
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			u = i + 1
			v = lst[i][j] 
			wt = matrix[i][lst[i][j] - 1]
			edgesHeap.Insert([u,v], wt)
	result = edgesHeap.HeapSort()
	sorted_edges = result[1]

	lst1, lst2 = [], []
	for i in range(verts_num + 1): lst1.append(vertex.Vertex(i))
	for i in range(verts_num + 1): lst2.append(i)
	MST = graph.Graph(verts_num)
	MST.add_vertices(lst2[1:])
	p, rank = [], []
	dad = np.zeros(verts_num+1)
	dad1 = np.zeros(verts_num+1)
	for i in range(verts_num+1):
		p.append(0)
		rank.append(0)
		
	def Find(v):
		w = v
		while(p[w]!=0): w = p[w]
		return w

	def Union(r1, r2):
		if(rank[r1] < rank[r2]): p[r1] = r2
		if(rank[r1] > rank[r2]): p[r2] = r1
		if(rank[r1] == rank[r2]):
			p[r1] = r2
			rank[r2] = rank[r2] + 1

	sign = []
	for i in range(verts_num + 1): sign.append(0)
	sign[0] = -1
	
	while len(sorted_edges)!=0 and sign.count(1) != verts_num:
		s_edge = sorted_edges.pop(0)
		u = s_edge[0]
		v = s_edge[1]
		r_u = Find(u)
		r_v = Find(v)
		if r_u != r_v:
			dad[v] = u
			dad1[u] = v
			MST.add_edge_mst(lst1[u],lst1[v])
			sign[u] = sign[v] = 1
			Union(r_u, r_v)
	
	mst_adj_list = (MST.adjacencyList())
	mst_adj_list.insert(0, [])

	current = s
	queue = []
	status = np.zeros(verts_num + 1)

	status[s] = 1
	queue.append(s)

	path =[]
	dad = np.zeros(verts_num)
		
	while current != t:
		current = queue.pop(0)
		path.append(current)
		for i in range(len(mst_adj_list[current])):
			nxt = mst_adj_list[current][i]
			if status[nxt] == 0:
				queue.append(nxt)
				status[nxt] = 1
				dad[nxt - 1] = current - 1
	max_bandwidth_path = path_represent(dad,matrix,s,t)
	print('[Solution 3] Max Bandwidth Path: Kruskal with Heap Sort: ')
	print('    Max Bandwidth: ' + str(max_bandwidth_path[1]) + '\n    Max Bandwidth Path:' + str(max_bandwidth_path[0]) + '\n    S-T path: (' + str(s + 1) + ' ' + rightArrow + ' ' + str(t + 1) + ')')
