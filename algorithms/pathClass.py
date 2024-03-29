import sys
import json
import numpy as np

class pathfinder:

    def __init__(self):
        vertices = 72
        self.V = vertices

        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

        emptyGraph = []

        with open('assets/files/Adjacency_Matrix') as f:
            lines = f.read().splitlines()
            for line in lines:
                emptyGraph.append(list(map(int, line.split(','))))

        self.sector_names = np.loadtxt('assets/files/sector_names.csv', delimiter=",", dtype=str)

        #Remove empty data in csv
        self.sector_names = np.delete(self.sector_names, 0, 0)


        self.graph = emptyGraph

    """
    def loadgraph(self):

        with open ('C:/Users/Diego/PycharmProjects/SafeNav/assets/files/Adjacency_Matrix') as f:
            print("loading")
            lines = f.read().splitlines()

        for line in lines:
            self.emptyGraph.append(list(map(int, line.split(','))))
    """

    def printweight(self, dist, target):
        return dist[target]

    def getShortestPath(self, distances, previous, targetIndex):

        path = []

        # Handle errors if path does not exist
        if (distances[targetIndex] == sys.maxsize):
            return path
        at = targetIndex
        # Goes to index of previous list to find what element came before
        while at is not None:
            path.append(at)
            at = previous[at]
        # Since it goes from the end to the source the list is reversed
        path.reverse()
        return path

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src, target):

        # list of lengths filled with infinites
        dist = [sys.maxsize] * self.V
        # List of previous node used to track the path
        prev = [None] * self.V
        # Initialization of the source
        dist[src] = 0
        # Tracks if the node has been visited before
        sptSet = [False] * self.V
        # Iterates 847 times

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
            # print(x)
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            # Iterates lots of times
            for y in range(self.V):
                # Checks the neighbors of the node
                '''
                self.graph[x][y] > 0
                Checks if the element of the matrix is a neighbor of the proposed node
                
                sptSet[y] == False
                Confirms if the node has been visited before
                
                dist[y] > dist[x] + self.graph[x][y]
                Compares if the weight of the new node is higher than the sum of the previous weights taken to arrive 
                there
                '''
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    # Adds the previous node to the path list
                    prev[y] = x
                    # The new node's weight is inserted into the list as the sum of the current node with the weight of the path to arrive there
                    dist[y] = dist[x] + self.graph[x][y]

        return self.printweight(dist, target), self.getShortestPath(dist, prev, target)

    def gptDecoder(self, gptout):
        try:
            if isinstance(gptout, str):
                gptout = json.loads(gptout)
            start_node, end_node = gptout["start_node"], gptout["end_node"]
            weight, path = self.dijkstra(start_node, end_node)
            named_path = []
            for node in path:
                named_path.append(self.sector_names[node, 1])
                named_path.append("-->")
            return named_path[:-1]

        except KeyError as k:
            print("GPT JSON didnt find the key", k)
        except Exception as e:
            print("Error in gptDecoder", e)

"""
#Example of how to implement code in main

test = pathfinder()
#a = {"start_node": 68, "end_node": 10}
#test.gptDecoder(a)
"""

