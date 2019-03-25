'''
Graph is an edge list.
Return path if it exists, else return None.
'''
def Hamiltonian(G, start = None, end = None, cycle = False):
    if cycle:
        path = [None] * ((len(G) + 1) if len(G) > 1 else 1)
        path[0] = start if start else 0
        visited = [False] * len(G)
        visited[path[0]] = True
        return _ham_cycle(G, path, visited, 0)
    elif start:
        path = [None] * len(G)
        path[0] = start
        visited = [False] * len(G)
        visited[path[0]] = True
        if end: return _ham_end(G, path, visited, 0, end)
        else: return _ham(G, path, visited, 0)
    else:
        if end:
            for v in range(len(G)):
                path = [None] * len(G)
                path[0] = start
                visited = [False] * len(G)
                visited[path[0]] = True
                if _ham_end(G, path, visited, 0, end): return path
        else:
            for v in range(len(G)):
                path = [None] * len(G)
                path[0] = v
                visited = [False] * len(G)
                visited[path[0]] = True
                if _ham(G, path, visited, 0): return path
        return None

'''
Find Hamiltonian path starts with the current path
'''
def _ham(G, path, visited, curr):
    if path[-1]: return path
    for v in G[path[curr]]:
        if not visited[v]:
            curr += 1
            path[curr] = v
            visited[v] = True
            if _ham(G, path, visited, curr): return path
            visited[v] = False
            path[curr] = None
            curr -= 1
    return None

'''
a path that end with some vertex
'''
def _ham_end(G, path, visited, curr, end):
    if path[-1]: return path
    for v in G[path[curr]]:
        if not visited[v] and (v != end or curr == len(G) - 2):
            curr += 1
            path[curr] = v
            visited[v] = True
            if _ham_end(G, path, visited, curr, end): return path
            visited[v] = False
            path[curr] = None
            curr -= 1
    return None

'''
a ham cycle
'''
def _ham_cycle(G, path, visited, curr):
    if path[-1]: return path
    for v in G[path[curr]]:
        if not visited[v] or v == path[0] and curr == len(G) - 1:
            curr += 1
            path[curr] = v
            visited[v] = True
            if _ham_cycle(G, path, visited, curr): return path
            visited[v] = False
            path[curr] = None
            curr -= 1
    return None
