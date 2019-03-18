'''
Graph is an edge list.
Return path if it exists, else return None.
'''
def Hamiltonian(G):
    if len(path) == n: return path
    for i in range(n):
        if graph[path[-1]][i] and i not in visited:
            visited.add(i)
            path.append(i)
            solution = Hamiltonian()
            if solution: return solution
            path.pop()
            visited.remove(i)
    return None
