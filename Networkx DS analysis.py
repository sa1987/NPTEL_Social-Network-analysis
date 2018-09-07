import networkx as nx
import matplotlib.pyplot as plt

G= nx.read_edgelist(r"C:\Users\assurend\Documents\NPTEL\Freemans_EIES-3_n32.txt")
G= nx.read_weighted_edgelist(r"C:\Users\assurend\Documents\NPTEL\Freemans_EIES-3_n32.txt")
print (nx.info(G))

print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))

print(nx.is_directed(G))

G= nx.read_pajek(r"C:\Users\assurend\Documents\NPTEL\karate.paj")

print (nx.info(G))

print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))

print(nx.is_directed(G))



G= nx.read_graphml(r"C:\Users\assurend\Documents\NPTEL\sample-social-network-datasets-master\sample-social-network-datasets-master\sample-datasets\marvel\marvel-network.graphml")

print (nx.info(G))

print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))

print(nx.is_directed(G))

G= nx.read_gexf(r"C:\Users\assurend\Documents\NPTEL\dh11.gexf")

print (nx.info(G))

print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))

print(nx.is_directed(G))

G= nx.read_gml(r"C:\Users\assurend\Documents\NPTEL\karate.gml")

print (nx.info(G))

print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))

print(nx.is_directed(G))




nx.draw(G)

nx.degree(G).values()

# plot defree distribution

def plot_deg_dist(G):
	my_degrees=nx.degree(G)
	#all_degrees=list(nx.degree(G).values()) #DegreeView isn't a dictionary (in NetworkX 2.1), but it is an iterator over (node, degree) pairs.
	all_degrees=list(dict(nx.degree(G)).values())
	all_unique_degrees = list(set(all_degrees))
	
	count_degrees = []
	for i in all_unique_degrees:
		x = all_degrees.count(i)
		count_degrees.append(x)
	print(all_unique_degrees)
	print(count_degrees)
	plt.plot(all_unique_degrees,count_degrees)
	plt.show()
	
#To check the powerlog 
plt.loglog(G)

density=nx.density(G)
clustering_coeff= nx.clustering(G)
nx.average_clustering(G)

#Diameter:

nx.diameter(G)


