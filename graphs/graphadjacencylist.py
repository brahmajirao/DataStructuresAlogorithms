"""
Implementation of a Graph as an Adjacency List
Using dictionaries, it is easy to implement the adjacency list in Python.
In our implementation of the Graph abstract data type we will create two classes: Graph,
which holds the master list of vertices, and Vertex, which will represent each vertex in the graph.

Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the
 of each edge. This dictionary is called connectedTo. The constructor simply initializes the id,
 which will typically be a string, and the connectedTo dictionary.
 The addNeighbor method is used add a connection from this vertex to another.
 The getConnections method returns all of the vertices in the adjacency list,
 as represented by the connectedTo instance variable. The getWeight method returns the weight of
 the edge from this vertex to the vertex passed as a parameter.
"""
class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: '+str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

"""
In order to implement a Graph as an Adjacency List what we need to do is define the methods our 
Adjacency List object will have:

    Graph() creates a new, empty graph.
    addVertex(vert) adds an instance of Vertex to the graph.
    addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
    addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
    getVertex(vertKey) finds the vertex in the graph named vertKey.
    getVertices() returns the list of all vertices in the graph.
in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
"""

class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not  in self.vertList:
            nv = self.add_vertex(t)
        self.vertList[f].add_neighbor(self.vertList[t], cost)

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vertList)
    g.addEdge(0,1,2)
    for vertex in g:
        print(vertex)
        print(vertex.get_connections())
        print('\n')