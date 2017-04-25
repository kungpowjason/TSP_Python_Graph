import networkx as nx
import matplotlib.pyplot as plt


n_nodes1 = ['v1', 'v2', 'v3', 'v4'];
edge_list1 = [('v1', 'v2', 2), ('v1', 'v3', 9), ('v2', 'v1', 1), ('v2', 'v4', 4), ('v2', 'v3', 6), ('v3', 'v2', 7), ('v3', 'v4', 8), ('v4', 'v2', 3),
('v4', 'v1', 6)];

n_nodes2 = ['v1', 'v2', 'v3', 'v4', 'v5'];
edge_list2 = [('v1', 'v2', 14),('v1', 'v3', 4),('v1', 'v4', 10),('v1', 'v5', 20),
('v2', 'v1', 14), ('v2', 'v3', 7), ('v2', 'v4', 8), ('v2', 'v5', 7),
('v3', 'v1', 4), ('v3', 'v2', 5), ('v3', 'v4', 7), ('v3', 'v5', 16),
('v4', 'v1', 11), ('v4', 'v2', 7), ('v4', 'v3', 9), ('v4', 'v5', 2),
('v5', 'v1', 18), ('v5', 'v2', 7), ('v5', 'v3', 17),('v5', 'v4', 4) ]

G = nx.MultiDiGraph();
G.add_nodes_from(n_nodes2);
G.add_weighted_edges_from(edge_list2);
G.degree(weight='weight');

open_list = n_nodes2;
candidate_solutions = [];
arr_solutions = [];


def findPath():
	for n, nbrs in G.adjacency_iter():
	    for nbr, eattr in nbrs.items():
	    	if nbr in open_list:
	    		open_list.remove(nbr)
	    		GG.add_edge(n, nbr, weight=minvalue)
	    		findPath();
	    	else:
	    		break;
	    break;


def findPath2(n, arr, op_list):
	neighbors = G.neighbors(n);
	isFound = False;
	t_weight = 0;
	for neighbor in neighbors:

		if neighbor in op_list:
			neigh_weight = G.get_edge_data(n, neighbor)[0]['weight'];
			if neighbor == 'v1' and len(op_list) == 1:
				arr.append(neighbor);
				op_list.remove(neighbor);
				isFound = True;
				t_weight = neigh_weight;
			elif neighbor != 'v1':
				arr.append(neighbor);
				op_list.remove(neighbor);
				(isFound, a_weight) = findPath2(neighbor, arr, op_list);
				t_weight = a_weight + neigh_weight;
		# if (isFound):
		# 	print ('neighbor ' + str(neighbor) + ' weight ' + str(neigh_weight));
		# 	break;
			# if (t_weight < min_weight):
			# 	best_neighbor = neighbor;
			# 	min_weight = t_weight;
	# if(isFound):
	# 	print ('neighbor ' + str(best_neighbor) + ' weight ' + str(min_weight));
	return (isFound, t_weight);


def findPath3(n, arr, op_list):
	neighbors = G.neighbors(n);
	isFound = False;
	t_weight = 0;
	ans_arr = [];
	best_neighbor = 'no best';
	min_weight = 500;
	for neighbor in neighbors:
		if neighbor in op_list:
			neigh_weight = G.get_edge_data(n, neighbor)[0]['weight'];
			if neighbor == 'v1' and len(op_list) == 1:
				arr.append(neighbor);
				op_list.remove(neighbor);
				isFound = True;
				t_weight = neigh_weight;
				return (isFound, t_weight, [neighbor]);
			elif neighbor != 'v1':
				arr.append(neighbor);
				op_list.remove(neighbor);
				ans_arr.append(neighbor);
				(isFound, a_weight, a_arr) = findPath3(neighbor, arr, op_list);
				ans_arr.extend(a_arr);
				t_weight = a_weight + neigh_weight;
		if (isFound):
		# 	print ('neighbor ' + str(neighbor) + ' weight ' + str(neigh_weight));
		# 	break;
			if (t_weight < min_weight):
				best_neighbor = neighbor;
				min_weight = t_weight;
	# if(isFound):
	# 	print ('neighbor ' + str(best_neighbor) + ' weight ' + str(min_weight));
	return (isFound, t_weight, ans_arr);


def findPath4(n, op_list):
	neighbors = G.neighbors(n);
	t_weight = 1000;
	best_arr = [];
	best_neighbor = 'no best';
	best_neighbor_weight = 100;
	min_weight = 500;
	found_flag = False;
	for neighbor in neighbors:
		isFound = False;
		new_op_list = list(op_list);
		if neighbor in op_list:
			neigh_weight = G.get_edge_data(n, neighbor)[0]['weight'];
			if neighbor == 'v1' and len(op_list) == 1:
				new_op_list.remove(neighbor);
				isFound = True;
				t_weight = neigh_weight;
				return (isFound, t_weight, [(neighbor, neigh_weight)]);
			elif neighbor != 'v1':
				new_op_list.remove(neighbor);
				(isFound, a_weight, a_arr) = findPath4(neighbor, new_op_list);
				if (isFound):
					found_flag = True;
				t_weight = a_weight + neigh_weight;
		if (isFound):
			if (t_weight < min_weight):
				best_neighbor = neighbor;
				best_neighbor_weight = neigh_weight;
				best_arr = a_arr;
				min_weight = t_weight;
	if(found_flag):
		best_arr.append((best_neighbor, best_neighbor_weight));
	return (found_flag, min_weight, best_arr);

def drawGraph():
	nx.draw_circular(G, with_labels=True);
	plt.show();

print (findPath4('v1', open_list));