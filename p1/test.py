def astar(start, end):
	opened_set = set(start)
	closed_set = set()

	g_cost = {}
	g_cost[start] = 100

	parent = {}
	parent[start] = start


	while 1:
		
		node = None
		for i in opened_set:
			if node == None or g_cost[i] + h_cost[i] < g_cost[node] + h_cost[node]:
				node = i

		# check if node is start_node
		if node == end:
			path = []
			while parent[node] != node:
				path.append(node)
				node = parent[node]
			
			path.append(start)
			path.reverse()
			return path

		for (neighbor, weight) in graph[node]:
			
			if neighbor not in opened_set and neighbor not in closed_set:
				
				opened_set.add(neighbor)
				parent[neighbor] = node
				g_cost[neighbor] = g_cost[node] + weight

			else:

				if g_cost[neighbor] > g_cost[node] + weight:
					g_cost[neighbor] = g_cost[node] + weight
					parent[neighbor] = node

					if neighbor in closed_set:
						closed_set.remove(neighbor)
						opened_set.add(neighbor)
		
		opened_set.remove(node)
		closed_set.add(node)

				


h_cost = {
	'A': 10,
	'B': 8,
	'C': 5,
	'D': 7,
	'E': 1,
	'F': 6,
	'G': 5,
	'H': 3,
	'I': 1,
	'J': 0,
}

graph = {
	'A': [ ('B', 6), ('F', 3) ],
	'B': [ ('C', 3), ('D', 2) ],
	'C': [ ('D', 1), ('E', 5) ],
	'D': [ ('C', 1), ('E', 8) ],
	'E': [ ('I', 5), ('J', 5) ],
	'F': [ ('G', 1), ('H', 7) ],
	'G': [ ('I', 3), ],
	'H': [ ('I', 2), ],
	'I': [ ('G', 5), ('J', 3) ],
}

print(astar('A', 'J'))