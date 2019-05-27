from copy import copy

class Graph:

    def __init__(self, directed = False, numVertices = 0):
        self.adjList = list()
        self.directed = directed
        for i in range(numVertices):
            self.addVertice()

    def addVertice(self):
        self.adjList.append(list())

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)

        if not self.directed:
            self.adjList[v2].append(v1)

    def removeEdge(self, v1, v2):
        self.adjList[v1].remove(v2)

        if not self.directed:
            self.adjList[v2].remove(v1)

    def numVertices(self):
        return len(self.adjList)

    def getVertices(self):
        return list(range(self.numVertices()))

    def numEdges(self):
        num = 0

        for edges in self.adjList:
            num = num + len(edges)

        if not self.directed:
            num = num / 2

        return num

    def degree(self, vertice):
        return len(self.adjList[vertice])

    def dfs(self, vertice, s = None):
        if s == None:
            s = set()

        s.add(vertice)

        for v in self.adjList[vertice]:
            if v not in s:
                self.dfs(v, s)

        return s

    def isConnected(self):
        return self.numVertices() == len(self.dfs(0))

    def isEulerian(self):
        for edges in self.adjList:
            if len(edges) % 2 != 0:
                return False

        return True

    def dfsCircuit(self, vertice, ini, ciclo):
        ciclo.append(vertice)

        if vertice == ini and self.numEdges() == 0:
            return True

        for v in copy(self.adjList[vertice]):
            self.removeEdge(vertice, v)
            if self.dfsCircuit(v, ini, ciclo):
                self.addEdge(vertice, v)
                return True

            self.addEdge(vertice, v)
            ciclo.pop()

    def eulerianCircuit(self, ini = 0):
        if not self.isConnected() or not self.isEulerian():
            return []
        
        ciclo = []
        self.dfsCircuit(ini, ini, ciclo)

        return ciclo

# Exemplo

graph = Graph(numVertices = 6)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)

print(graph.eulerianCircuit())

