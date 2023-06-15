def astar(start, stop):


	opened_set = set(start)
	closed_set = set()
		
	g_cost = {}
	g_cost[start] = 100

	parents = {}
	parents[start] = start

	
	while 1:
		node = None
		for i in opened_set:
			if node == None or g_cost[i] + h_cost[i] < g_cost[node] + h_cost[node]:
				node = i

		if node == stop:
			path = []
			while parents[node] != node:
				path.append(node)
				node = parents[node]
			
			path.append(start)
			path.reverse()
			return path

		for (neighbour, weight) in graph[node]:
			if neighbour not in opened_set and neighbour not in closed_set:
				opened_set.add(neighbour)
				g_cost[neighbour] = g_cost[node] + weight
				parents[neighbour] = node
			else:
				if g_cost[neighbour] > g_cost[node] + weight:
					g_cost[neighbour] = g_cost[node] + weight
					parents[neighbour] = node

					if neighbour in closed_set:
						closed_set.remove(neighbour)
						opened_set.add(neighbour)

		opened_set.remove(node)
		closed_set.add(node)




h_cost = {
    'A': 10,
    'B': 3,
    'C': 2,
    'D': 0
}

graph = {
    'A': [('B', 3),('C', 4)],
    'B': [('A', 5),('C', 5)],
    'C': [('D', 4)]
}

print(astar('A', 'D'))