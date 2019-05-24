
class Graph:

    def __init__(self, directed = False):
        self.adjList = dict()
        self.directed = directed

    def addVertice(self, vertice):
        self.adjList[vertice] = list()

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)

        if not self.directed:
            self.adjList[v2].append(v1)

    def degree(self, vertice):
        return len(self.adjList[vertice])

    # TODO
    def fleury():
        pass


# Exemplo

graph = Graph()

graph.addVertice(0)
graph.addVertice(1)
graph.addVertice(2)
graph.addVertice(3)

graph.addEdge(0, 1)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(2, 1)

print(graph.adjList)
