import requests
import geopandas as gdp
import pandas as pd
from libpysal import weights
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Calling HoyodeCrimen's API to retrieve a GEOJSON containing the polygons of Mexico City
url = requests.get("https://hoyodecrimen.com/api/v1/sectores/geojson")

#Converting the incoming data and checking the CRS format it comes with
filepath = url.text
cdmx = gdp.read_file(filepath)

#Conversion to Mexico City's CRS format
cdmx = cdmx.to_crs(6362)

df = pd.DataFrame(cdmx)

sector_list = df["sector"].unique()
sector_list.reshape(72,)

queen = weights.Queen.from_dataframe(cdmx)
mapCDMX = queen.to_networkx()

df_crime = pd.read_csv("C:/Users/Diego/PycharmProjects/SafeNav/assets/files/crimes new.csv")
a, b, c = df_crime["rows/crime"].to_numpy(), df_crime["rows/period2_count"].to_numpy() + np.ones((1460,), int), df_crime["rows/sector"].to_numpy()
parsed_crime = np.column_stack((a, b, c))

# Create an array of ones with the same length as df
ones_column = np.ones((sector_list.shape[0], 1))

# Concatenate df and zeros_column along a new axis
sector_crime = np.concatenate((np.expand_dims(sector_list, axis=1), ones_column), axis=1)


#Sum all the categories of crimes and assigning them to a specific crime
n = 0
for sector in sector_list:
    crime_count = 0
    for row in parsed_crime:
        if row[2] == sector:
            crime_count += row[1]
    sector_crime[n,1] = crime_count
    n+=1


# Function from NetworkX documentation
def all_neighbors(graph, node):
    """Returns all of the neighbors of a node in the graph.
    If the graph is directed returns predecessors as well as successors.
    Parameters
    ----------
    graph : NetworkX graph
    Graph to find neighbors.
    node : node
    The node whose neighbors will be returned.
    Returns
    -------
    neighbors : iterator
    Iterator of neighbors
    """
    if graph.is_directed():

        values = chain(graph.predecessors(node), graph.successors(node))
    else:
        values = graph.neighbors(node)
        return values

weighted_graph = nx.MultiDiGraph()

for node in mapCDMX:
    neighbors = list(all_neighbors(mapCDMX,node))
    for neighbor in neighbors:
        loc = np.where(sector_crime[:,0]== sector_list[neighbor])[0][0]
        weight = int(sector_crime[loc,1])
        weighted_graph.add_edge(node, neighbor, weight = weight)

weighted_dicts = nx.convert.to_dict_of_dicts(weighted_graph)
adjacency_matrix = np.zeros((72,72), dtype=int)
for x in range(72):
     single_dict = weighted_dicts[x]
     for key, value in single_dict.items(): #Key is np int, value is dict
         node, node_weight = int(key), value[0]["weight"]
         adjacency_matrix[x][node] = node_weight
np.savetxt('Adjacency_Matrix',adjacency_matrix, delimiter=',', fmt= '%d')

#Not my proudest implementation, but it works

