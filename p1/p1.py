# GRAPH  hardcode graph ds
# H_COST hardcode hcost values

# OPENED // the set of nodes to be evaluated
# add the start node to OPEN
# CLOSED // the set of nodes already evaluated

# create gcost
# set gcost of start to 0

# create gcost
# set gcost of start to 0

# loop
# 	current = node in OPEN with the lowest f cost
# 	remove current from OPEN
# 	add current to CLOSED

# 	if current is the target node // path has been found
# 		return
	
# 	foreach neighbour of the current node
# 		if neighbour is not traversable or neighbour is in CLOSED
# 		skip to the next neighbour

# 		if new path to neighbour is shorter OR neighbour is not in OPEN
# 			set f cost of neighbour
# 			set parent of neighbour to current
			
# 			if neighbour is not in OPEN
# 				add neighbour to OPEN


# ? simplified algo
"""
create opened_set
add start_node to opened_set

create closed_set

create g_cost dictionary
set start_nodes g_cost to 100

create parent_dictionary (to keep track of parents of node)
add start_node's parent as start_node

till path is found:

	1. chose node from opened_set such that it has least f_cost

	2.1 check if the chose node is stop_node:
			yes: 
				traverse parents and return resulted path
	
	2.2 check all of the neighbour_nodes of node
		if neighbor_node is not in closed and opened_set:
			- add to opened_node
			- update neighbour_nodes g_cost 
			- set parent of neighbour_node to node
		
		else:
			if g_cost of neighbour_node > g_cost of node:
				- update neighbour_nodes g_cost to g_cost of node 
				- set new parent of neighbour_node to node

				if neighbour was in closed_set:
					remove from closed-set
					add to opened-set

	
	3 	remove node from opened_node
		add node to closed_node
"""




def astar(start, stop):
	opened_set = set(start)
	closed_set = set()

	g_cost = {}
	g_cost[start] = 100

	parents = {}
	parents[start] = start

	while 1:

		# updating current shortest node
		node = None
		print(opened_set)
		for i in opened_set:
			if node == None or g_cost[i]+h_cost[i] < g_cost[node]+h_cost[node]:
				node = i
		
		if node == stop:
			path = []
			while parents[node] != node:
				print(node)
				path.append(node)
				node = parents[node]

			path.append(start)
			path.reverse()
			return path
		
		for (neighbour, weight) in graph[node]:

			# if we havent visited this node before
			if neighbour not in opened_set and neighbour not in closed_set: 
				# then add to opened_set update its parent and g_cost
				opened_set.add(neighbour)
				parents[neighbour] = node
				g_cost[neighbour] = g_cost[node] + weight
			else:
				   # old g_cost 	   # new g_cost 
				if g_cost[neighbour] > g_cost[node] + weight: # g_cost[node] + weight => the weight of the node traversed from a different parent
					g_cost[neighbour] = g_cost[node] + weight # updating new g_cost
					parents[neighbour] = node

					if neighbour in closed_set:
						closed_set.remove(neighbour)
						opened_set.add(neighbour)

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