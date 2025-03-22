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
