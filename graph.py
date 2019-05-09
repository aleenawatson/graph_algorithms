
"""

Creator: Aleena Watson
Creation date: 4-21-19

Graph structure represented as an adjacency list
of arrays. 

"""

# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.edge = 1
    # end
# end

# A class to represent a graph . A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [ [] for _ in range(self.V) ]
    # end
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        self.graph[src].append(node)
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        self.graph[dest].append(node)

        # Optional: Print array adjacencies as they are added
        # print([len(self.graph[i]) for i in range(self.V)])
    # end

    def delete_vertex(self, vertex):
        for i in range(self.V):
            if i != vertex:
                while vertex in self.graph[i]:
                    self.graph[i].remove(vertex)
                # end
            # end
        # end
        self.graph[vertex] = []

        for i in range(self.V):
            for j in self.graph[i]:
                # test: print vertices as you iterate
                # print("{} ".format(i), end="")
                # test: print neighbors as you iterate
                # print("{} ".format(j.vertex), end="")
                if j.vertex == vertex:
                    # test: did you make it into endpoints of deleted vertex?
                    # print("here")
                    self.graph[i].remove(j)
                # end
            # end
        # end
    # end

    def delete_edge(self, u, v):	
        for j in self.graph[u]:
            if j.vertex == v:
                self.graph[u].remove(j)
            # end
        # end
        for i in self.graph[v]:
            if i.vertex == u:
                self.graph[v].remove(i)
            # end
        # end

    # end

    def cycle_finder(self, src, dest):
        for i in range(self.V):
            for neighbor in self.graph[i]:
                continue
            # end
        # end
    #end

    def print_neighbors(self, vertex):
        print(vertex, ":")
        for neighbor in self.graph[vertex]:
            print("{}  ".format(neighbor.vertex), end="")
        # end
        print("\n")
    # end
  
    # Function to print the graph 
    def print_adjacencyLists(self): 
        for i in range(self.V): 
            # Print length of array of graph[i]
            # print(len(self.graph[i]))
            self.print_neighbors(i)
        # end
    # end
# end

# Petersen Graph
V = 10
pg = Graph(V) 
pg.add_edge(0, 1)
pg.add_edge(0, 4)
pg.add_edge(0, 5)
pg.add_edge(1, 2)
pg.add_edge(1, 6)
pg.add_edge(2, 3)
pg.add_edge(2, 7)
pg.add_edge(3, 4)
pg.add_edge(3, 8)
pg.add_edge(4, 9)
pg.add_edge(5, 7)
pg.add_edge(5, 8)
pg.add_edge(6, 8)
pg.add_edge(6, 9)
pg.add_edge(7, 9)

# petersen_graph.print_adjacencyList()
# petersen_graph.delete_vertex(8)
pg.delete_edge(0, 1)

pg.print_adjacencyLists()
#comment