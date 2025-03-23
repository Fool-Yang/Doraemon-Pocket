'''
# recursive DFS
def TopologicalSort(G, reverse=False):
    n = len(G)
    Stack = []
    Visited = [False]*n
    for u in range(n):
        if not Visited[u]:
            _dfs(G, u, Visited, Stack)
    return Stack if reverse else Stack[::-1]

def _dfs(G, s, Visited, Stack):
    Visited[s] = True
    for v in G[s]:
        if not Visited[v]:
            _dfs(G, v, Visited, Stack)
    Stack.append(s)
'''
# iterative DFS
# do not mark the neighbors as visited when they are pushed onto the stack
# that is a common mistake in iterative DFS
# that will stop them from getting visited from a deeper node
# the paths need to be as long as possible in topological sorting
# only do that in BFS to avoid adding a node twice
def TopologicalSort(G, reverse=False):
    n = len(G)
    Stack = []
    Visited = [False]*n
    for u in range(n):
        if not Visited[u]:
            DFS_Stack = [(u, True), (u, False)]
            while DFS_Stack:
                curr, returned = DFS_Stack.pop()
                if returned:
                    Stack.append(curr)
                elif not Visited[curr]:
                    Visited[curr] = True
                    for v in G[curr]:
                        if not Visited[v]:
                            DFS_Stack.append((v, True))
                            DFS_Stack.append((v, False))
    return Stack if reverse else Stack[::-1]
