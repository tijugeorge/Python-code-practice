

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print 'before add '+ str(visited)
    visited.add(start)
    print 'after add '+ str(visited)
    for next in graph[start] - visited:
        print 'start '+ str(start)
        print 'inside for '+ str(graph[start])
        dfs(graph, next, visited)
    return visited



print dfs(graph, 'A')