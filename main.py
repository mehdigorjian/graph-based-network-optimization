import time, random, graph_generator, routing_algorithms
pair_iteration = 5

print('----------INITIALIZING GRAPH----------')
option = int(input('Selection options: \n    [1] G1 Graph \n    [2] G2 Graph\nEnter option: '))

if option == 1:
	print('--------------------------------------------')
	verts_num = int(input('Enter Graph type G1 Nodes Number: '))
	g = graph_generator.graph1(verts_num)

if option == 2:
	print('--------------------------------------------')
	verts_num = int(input('Enter Graph type G2 Nodes Number: '))
	g = graph_generator.graph2(verts_num)

if option == 1 or option == 2:
	duration_param = ''
	time1, time2, time3 = 0, 0, 0
	
	print('--------------------------------------------')
	print('[info] Testing Process Started...')
	print('--------------------------------------------\n')

	for i in range(pair_iteration):
		print('------------iteration pair ' + str(i+1) + ' -------------')
		duration_param += 'Dijkstra without Heap | Dijkstra with Heap | Kruskal with Heapsort\n'
		s1 = random.randint(1, verts_num)
		t1 = s1
		while t1 == s1: t1 = random.randint(1, verts_num)
		
		start = time.time()
		routing_algorithms.dijkstra_no_heap(g, s1, t1)
		time1 = time1 + time.time() - start
		duration_param = duration_param + str(time.time() - start) + '         '	
		
		start = time.time()
		routing_algorithms.dijkstra_heap(g, s1, t1)
		time2 = time2 + time.time() - start
		duration_param = duration_param + str(time.time() - start) + '         '
		
		start = time.time()
		routing_algorithms.kruskal_heapsort(g, s1, t1)
		time3 = time3 + time.time() - start
		duration_param = duration_param + str(time.time() - start) + '        \n'
	
	print('-------------------------Algorithm Run Time--------------------------')
	print(duration_param)
	print('-----------------------------Run Ended!------------------------------')
