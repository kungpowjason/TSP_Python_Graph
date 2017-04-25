import networkx as nx
import matplotlib.pyplot as plt
import math

# Traveling Sales Person Algorithm Class
class TSP_Algorithm:
	"""Implementation of solution to traveling sales person problem,
	The algorithm is basically a breadth first search that prunes trees that
	have visited a node already encountered.

    """

	def __init__(self, G, home):
		self.G = G; #Graph
		self.home = home; #Home City (node in graph)
		self.open_list = self.G.nodes(); #A list of all nodes in graph

	# findPath: recursively finds a path that visits every node once and returns back to the starting city
	# params:
	#	n : current node
	#	op_list : nodes left to explore
	def findPath(self, n, op_list): 
		neighbors = self.G.neighbors(n); #get neighbors of current node
		t_weight = math.inf #total weight (initialize to inf)
		# declare and initialize best variables out of the options
		best_arr = [];
		best_neighbor = 'no best';  
		best_neighbor_weight = math.inf;
		min_weight = math.inf;
		found_flag = False; # flag indicating if a solution has been found in any neighbor
		for neighbor in neighbors:
			isFound = False; # initialize individual found flag to False
			new_op_list = list(op_list); # create a copy of the nodes left to go
			# if the current neighbor a potential route to take, proceed to recursive call
			if neighbor in op_list:
				neigh_weight = self.G.get_edge_data(n, neighbor)[0]['weight']; #get weight of the edge to this option
				# CASE 1: visited all nodes and the home city is last
				if neighbor == self.home and len(op_list) == 1:
					new_op_list.remove(neighbor);
					isFound = True;
					t_weight = neigh_weight;
					return (isFound, t_weight, [(neighbor, neigh_weight)]);
				# CASE 2: haven't visited all nodes so continue rescurve call
				elif neighbor != self.home:
					new_op_list.remove(neighbor);
					(isFound, a_weight, a_arr) = self.findPath(neighbor, new_op_list);
					if (isFound):
						found_flag = True;
					t_weight = a_weight + neigh_weight;
				# CASE 3: node already has been visited
				# don't do anything and keep found flag to FALSE
			# Essential this just keeps track of the best option to take
			if (isFound):
				if (t_weight < min_weight):
					best_neighbor = neighbor;
					best_neighbor_weight = neigh_weight;
					best_arr = a_arr;
					min_weight = t_weight;
		# add the best option to the solution path (best_arr)
		if(found_flag):
			best_arr.append((best_neighbor, best_neighbor_weight));
		# return the accumulated solution path bro
		return (found_flag, min_weight, best_arr);

	#Prints the solution in a pretty output.
	def printSolutionPath(self):
		# Get data
		(isFound, t_weight, solution_path) = self.findPath(self.home, self.open_list);
		# Print Data if solution is found
		if(isFound):
			print ('Starting home city: ' + self.home);
			j = 0;
			for i in reversed(solution_path):
				j += 1;
				print ('Visit ' + str(j) + ' City : ' + str(i));
			print ('Total Cost of Trip: ' + str(t_weight));
		else:
			print ('A solution has not been found.');

	# Draws a visual graph of the node setup
	# Note: doesn't show solution paths
	def drawGraph(self):
		nx.draw_circular(G, with_labels=True);
		plt.show();


# Test Program for TSP Solution
def main():

	# Setting up Nodes and Edges for Graph 2
	n_nodes1 = ['v1', 'v2', 'v3', 'v4'];

	edge_list1 = [('v1', 'v2', 2), ('v1', 'v3', 9), ('v2', 'v1', 1), ('v2', 'v4', 4), ('v2', 'v3', 6), ('v3', 'v2', 7), ('v3', 'v4', 8), ('v4', 'v2', 3),
	('v4', 'v1', 6)];

	# Setting up Nodes and Edges for Graph 3 (Converting from adjacency matrix)
	n_nodes2 = ['v1', 'v2', 'v3', 'v4', 'v5'];

	edge_list2 = [('v1', 'v2', 14),('v1', 'v3', 4),('v1', 'v4', 10),('v1', 'v5', 20),
	('v2', 'v1', 14), ('v2', 'v3', 7), ('v2', 'v4', 8), ('v2', 'v5', 7),
	('v3', 'v1', 4), ('v3', 'v2', 5), ('v3', 'v4', 7), ('v3', 'v5', 16),
	('v4', 'v1', 11), ('v4', 'v2', 7), ('v4', 'v3', 9), ('v4', 'v5', 2),
	('v5', 'v1', 18), ('v5', 'v2', 7), ('v5', 'v3', 17),('v5', 'v4', 4) ]

	# Setting up a Directed Graph
	G = nx.MultiDiGraph();
	G.add_nodes_from(n_nodes2);
	G.add_weighted_edges_from(edge_list2);
	G.degree(weight='weight');

	#Establish home city
	home_city = 'v1';

	#Create instance of TSP_Algorithm
	tsp = TSP_Algorithm(G, home_city);

	#Print Solution	
	tsp.printSolutionPath();

if __name__ == '__main__':
	main();