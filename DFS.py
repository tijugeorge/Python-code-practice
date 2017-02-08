from collections import defaultdict

class Graph(object):
    def __init__(self):
        """Default dictionary"""
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        """This is the function to add an edge to the graph. u is the key and v
        or graph[u] is the value"""
        self.graph[u].append(v)

    def BFS(self, s):
        """Fucntion to print BS of the graph"""
        visited = [False]*(len(self.graph)) #marking those visited vertices
        queue = [] #queue created for BFS
        queue.append(s) #mark the source code as visited and enqueue it
        visited[s] = True
        while queue:
            s = queue.pop(0)#dequeue a vertex from queue and print it
            print s,

            for i in self.graph[s]:
                if visited[i] == False: # get all the adjacent vertices of the
                #dequeued vertex s, if a ajacent has not been visited, then mark
                #it visited and enqueue it
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print 'Breadth first traversal when the vertex is 1'
g.BFS(3)
