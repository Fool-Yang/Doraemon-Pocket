def FloydWarshall(G):
    n = len(G)
    inf = float("inf")
    neg_inf = -inf
    Dist = [[inf]*n for _ in range(n)]
    Prev = [[None]*n for _ in range(n)]
    for u in range(n):
        Edges_from_u = G[u]
        for v in Edges_from_u:
            Dist[u][v] = Edges_from_u[v]
            Prev[u][v] = u
        if Dist[u][u] > 0: # in case there are self loops
            Dist[u][u] = 0
    for j in range(n):
        for i in range(n):
            if Dist[i][j] < inf: # this if statement can reduce runtime
                for k in range(n):
                    new_dist = Dist[i][j] + Dist[j][k]
                    if new_dist < Dist[i][k]:
                        Dist[i][k] = new_dist
                        Prev[i][k] = Prev[j][k]
    # check for neg-cycle
    for j in range(n):
        if Dist[j][j] < 0:
            for i in range(n):
                if Dist[i][j] < inf:
                    for k in range(n):
                        if Dist[j][k] < inf:
                            Dist[i][k] = neg_inf
    return Dist, Prev
