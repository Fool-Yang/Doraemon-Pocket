def BellmanFord(G, s):
    n = len(G)
    inf = float("inf")
    neg_inf = -inf
    Dist = [inf]*n
    Dist[s] = 0
    Prev = [None]*n
    for _ in range(n - 1):
        # for each edge (u, v)
        for u in range(n):
            Edges_from_u = G[u]
            for v in Edges_from_u:
                new_dist = Dist[u] + Edges_from_u[v]
                if new_dist < Dist[v]:
                    Dist[v] = new_dist
                    Prev[v] = u
    # check for neg-cycle
    Neg_inf = []
    for u in range(n):
        Edges_from_u = G[u]
        for v in Edges_from_u:
            if Dist[u] + Edges_from_u[v] < Dist[v]:
                Dist[v] = neg_inf
                Neg_inf.append(v)
    for u in Neg_inf:
        Q = [u]
        while Q:
            u = Q.pop()
            for v in G[u]:
                if Dist[v] != neg_inf:
                    Q.append(v)
                    Dist[v] = neg_inf
    return Dist, Prev
