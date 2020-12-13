import sys
from pythonds.basic import Queue

"""
A vertex Abstract Data Type representing a vertex and its related details.
A vertex holds an id that identifies it and a reference to the other vertices it is connected to. 
For the sake of the graph traversal algoritv
v
vhms, we add extra attributes(instance variables) like colour, previous, etc. 
This is done to keep track of a vertex that has been visited as we traverse through the graph. Making it easier to 
visualise the result of the traversal process.  
"""
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

# Adding a neighbor to vertex/node
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

# overriding the str dunder to allow for reperesention of the vertex 
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

# gets all the other vertex a vertex is connected to
    def getConnections(self):
        return self.connectedTo.keys()

# returns the id of a vertex 
    def getId(self):
        return self.id

# returns the weight of a vertex
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# sets the colour for a particular vertex
    def setColor(self,color):
        self.color = color


    def setPred(self,p):
        self.pred = p

    def getPred(self):
        return self.pred
        
    def setDistance(self,d):
        self.dist = d
        pass
 
    def setDiscovery(self,dtime):
        self.disc = dtime
        pass
        
    def setFinish(self,ftime):
        self.fin = ftime
        pass
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    


"""
Astract Data Type implementation for a graph. A graph consist of multiple vertices which is stored in a doctionary. 
A variable also keeps track of the number of vertices a graph has.
"""
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

# adding a vertex to the graph. This increments vertex count, makes an instance of vertex class and adds it to the vertices list
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

# on given a key, checks whether a vertex with that key exist exist in the graph, and returns the vertex else returns none
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

# checks if a particular veretx exist in the graph and returns a boolean vakue
    def __contains__(self,n):
        return n in self.vertList

# adds an edges to two vertcies ensentially connecting them together 
    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

# returns all the keys of the vertices present in the graph 
    def getVertices(self):
        return self.vertList.keys()

# dunder method to override the iterable method. making it possible to easily loop through the graph
    def __iter__(self):
        return iter(self.vertList.values())


# recursive implementaion of depth first search
    def depthFirstSearch(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.depthFirstSearch(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

# itetative implemetation of breath first search 
    def breathFirstSearch(self, startVertex):
        startVertex.setDistance(0)
        startVertex.setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(startVertex)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')






"""
Examples:
"""

#creating an instance of our base graph class  
ourGraph = Graph()

# adding a vertex of numbers 0 - 8 into the graph
for i in range(9):
    ourGraph.addVertex(i)

ourGraph.addEdge(0,1,5)
ourGraph.addEdge(0,5,2)
ourGraph.addEdge(1,2,4)
ourGraph.addEdge(2,3,9)
ourGraph.addEdge(3,4,7)
ourGraph.addEdge(3,5,3)
ourGraph.addEdge(4,0,1)
ourGraph.addEdge(5,4,8)
ourGraph.addEdge(5,2,1)
ourGraph.addEdge(6,4,1)
ourGraph.addEdge(7,5,1)
ourGraph.addEdge(8,2,1)

# exploring the cedges of the vertices in our graph
for vertex in ourGraph:
    for connection in vertex.getConnections():
        print("( %s , %s )" % (vertex.getId(), connection.getId()))

#breathFirstSearch search of our graph
startingVertex = ourGraph.getVertex(2)
print(ourGraph.getVertices())
ourGraph.breathFirstSearch(startingVertex)
ourGraph.depthFirstSearch(startingVertex)