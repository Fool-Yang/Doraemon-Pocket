"""
This algorithm has two versions, one uses Dinic and the other doesn't.
Theoretically Dinic should be faster but it may depend on the graph.
"""
# Ford-Fulkerson with Dijkstra for computing the min cost flow
def SuccessiveShortestPath(G, C, s, t):
    n = len(G)
    inf = float("inf")
    # construct residual graph with flow/cap
    Gr = [{} for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            Gr[u][v] = [0, G[u][v]]
            if u not in Gr[v]: # do not overwrite existing edges
                Gr[v][u] = [0, 0]
    # find the potential of each vertex (Johnson's algorithm)
    Potential = BellmanFord(C, s)
    # find augmenting path until fails
    total_flow = total_cost = 0
    augmenting_path_found = True
    while augmenting_path_found:
        # build the potential graph so the edge weights are non-negative
        Gp = [{} for _ in range(n)]
        for u in range(n):
            for v in Gr[u]:
                flow, cap = Gr[u][v]
                if flow < 0: # can push back flow on the reverse edge
                    Gp[u][v] = Potential[u] - Potential[v] - C[v][u]
                elif flow < cap:
                    Gp[u][v] = Potential[u] - Potential[v] + C[u][v]
        # find the cheapest augmenting path on the potential graph
        Potential_Cost, Prev = Dijkstra(Gp, s)
        # update potentials to reflect the cost on the residual graph
        for u in range(n):
            Potential[u] += Potential_Cost[u]
        augmenting_path_found = Potential[t] < inf
        if augmenting_path_found:
            # find bottleneck
            inc = inf
            curr = t
            while curr != s:
                flow, cap = Gr[Prev[curr]][curr]
                if flow < 0:
                    room = -flow
                else:
                    room = cap - flow
                if room < inc:
                    inc = room
                curr = Prev[curr]
            # push more flow
            curr = t
            while curr != s:
                Gr[Prev[curr]][curr][0] += inc
                Gr[curr][Prev[curr]][0] -= inc
                curr = Prev[curr]
            total_flow += inc
            total_cost += inc*Potential[t]
    return Gr, total_flow, total_cost

def BellmanFord(G, s):
    n = len(G)
    inf = float("inf")
    neg_inf = -inf
    Dist = [inf]*n
    Dist[s] = 0
    for _ in range(n - 1):
        # for each edge (u, v)
        for u in range(n):
            if Dist[u] < inf: # this if statement can reduce runtime
                Edges_from_u = G[u]
                for v in Edges_from_u:
                    new_dist = Dist[u] + Edges_from_u[v]
                    if new_dist < Dist[v]:
                        Dist[v] = new_dist
    # no need to check for neg-cycle as we cannot have cyclic flow
    return Dist

def Dijkstra(G, s):
    n = len(G)
    Dist = [float("inf")]*n
    Dist[s] = 0
    Prev = [None]*n
    H = [list(range(n)), {i: i for i in range(n)}]
    H[0][0], H[0][s] = s, 0
    H[1][0], H[1][s] = s, 0
    while H[0]:
        u = _remove_min(H, Dist)
        Edges_from_u = G[u]
        for v in Edges_from_u:
            new_dist = Dist[u] + Edges_from_u[v]
            if new_dist < Dist[v]:
                Dist[v] = new_dist
                Prev[v] = u
                _update(H, Dist, v)
    return Dist, Prev

# indexed min heap operations
def _remove_min(H, Data):
    heap, index = H
    top = heap[0]
    heap[0] = heap[-1]
    last, curr = 0, 1
    while curr < len(heap):
        if curr + 1 < len(heap) and Data[heap[curr + 1]] < Data[heap[curr]]:
            curr += 1
        if Data[heap[curr]] < Data[heap[last]]:
            heap[curr], heap[last] = heap[last], heap[curr]
            index[heap[last]] = last
        else:
            break
        last, curr = curr, curr*2 + 1
    index[heap.pop()] = last
    del index[top]
    return top

def _update(H, Data, elem):
    heap, index = H
    curr = index[elem]
    while curr:
        parent = (curr - 1)//2
        if Data[heap[curr]] < Data[heap[parent]]:
            heap[curr], heap[parent] = heap[parent], heap[curr]
            index[heap[curr]] = curr
        else:
            break
        curr = parent
    index[heap[curr]] = curr

"""
==========================================================================================================
"""

# A primal-dual algorithm (Dinic with Dijkstra using Johnson's potentials for computing the min cost path)
def SuccessiveShortestPath(G, C, s, t):
    n = len(G)
    inf = float("inf")
    # construct residual graph with flow/cap
    Gr = [{} for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            Gr[u][v] = [0, G[u][v]]
            if u not in Gr[v]: # do not overwrite existing edges
                Gr[v][u] = [0, 0]
    # find the potential of each vertex (Johnson's algorithm)
    Potential = BellmanFord(C, s)
    # find augmenting path until fails
    total_flow = total_cost = 0
    augmenting_path_found = True
    while augmenting_path_found:
        # build the potential graph so the edge weights are non-negative
        Gp = [{} for _ in range(n)]
        for u in range(n):
            for v in Gr[u]:
                flow, cap = Gr[u][v]
                if flow < 0: # can push back flow on the reverse edge
                    Gp[u][v] = Potential[u] - Potential[v] - C[v][u]
                elif flow < cap:
                    Gp[u][v] = Potential[u] - Potential[v] + C[u][v]
        # build the shortest-path subgraph
        Potential_Cost, Gs = Dijkstra(Gp, s)
        # update potentials to reflect the cost on the residual graph
        for u in range(n):
            Potential[u] += Potential_Cost[u]
        # calculate the free room (width) of each edge in the subgraph
        for u in range(n):
            for v in Gs[u]:
                flow, cap = Gr[u][v]
                if flow < 0:
                    room = -flow
                else:
                    room = cap - flow
                Gs[u][v] = room
        # build the level graph with BFS
        Level = [-1]*n # distance to source in number of edges
        Level[s] = 0
        BFS_Queue = deque([s])
        while BFS_Queue:
            u = BFS_Queue.popleft()
            for v in Gs[u]:
                if Level[v] == -1:
                    Level[v] = Level[u] + 1
                    BFS_Queue.append(v)
        augmenting_path_found = Level[t] != -1
        if augmenting_path_found:
            # send flow along all path with DFS
            more_flow = True
            while more_flow:
                more_flow = _send_flow(Gr, Gs, Level, inf, s, t)
                total_flow += more_flow
                total_cost += more_flow*Potential[t]
    return Gr, total_flow, total_cost

def _send_flow(Gr, Gs, Level, input_flow, u, t):
    if u == t:
        return input_flow
    total_output_flow = 0
    for v in Gs[u]:
        room = Gs[u][v]
        # the level graph creates a DAG
        if Level[v] == Level[u] + 1 and room > 0:
            output_flow = input_flow
            # find bottleneck
            if room < output_flow:
                output_flow = room
            output_flow = _send_flow(Gr, Gs, Level, output_flow, v, t)
            if output_flow:
                Gr[u][v][0] += output_flow
                Gr[v][u][0] -= output_flow
                Gs[u][v] -= output_flow
                total_output_flow += output_flow
                input_flow -= output_flow
    return total_output_flow

def BellmanFord(G, s):
    n = len(G)
    inf = float("inf")
    neg_inf = -inf
    Dist = [inf]*n
    Dist[s] = 0
    for _ in range(n - 1):
        # for each edge (u, v)
        for u in range(n):
            if Dist[u] < inf: # this if statement can reduce runtime
                Edges_from_u = G[u]
                for v in Edges_from_u:
                    new_dist = Dist[u] + Edges_from_u[v]
                    if new_dist < Dist[v]:
                        Dist[v] = new_dist
    # no need to check for neg-cycle as we cannot have cyclic flow
    return Dist

# this version of Dijkstra also returns the shortest-path subgraph
def Dijkstra(G, s):
    n = len(G)
    Dist = [float("inf")]*n
    Dist[s] = 0
    Prev = [None]*n
    H = [list(range(n)), {i: i for i in range(n)}]
    H[0][0], H[0][s] = s, 0
    H[1][0], H[1][s] = s, 0
    while H[0]:
        u = _remove_min(H, Dist)
        Edges_from_u = G[u]
        for v in Edges_from_u:
            new_dist = Dist[u] + Edges_from_u[v]
            if new_dist < Dist[v]:
                Dist[v] = new_dist
                Prev[v] = u
                _update(H, Dist, v)
    # build the shortest-path subgraph
    Gs = [{} for _ in range(n)]
    for u in range(n):
        dist = Dist[u]
        for v in G[u]:
            if dist + G[u][v] == Dist[v]:
                Gs[u][v] = G[u][v]
    return Dist, Gs

# indexed min heap operations
def _remove_min(H, Data):
    heap, index = H
    top = heap[0]
    heap[0] = heap[-1]
    last, curr = 0, 1
    while curr < len(heap):
        if curr + 1 < len(heap) and Data[heap[curr + 1]] < Data[heap[curr]]:
            curr += 1
        if Data[heap[curr]] < Data[heap[last]]:
            heap[curr], heap[last] = heap[last], heap[curr]
            index[heap[last]] = last
        else:
            break
        last, curr = curr, curr*2 + 1
    index[heap.pop()] = last
    del index[top]
    return top

def _update(H, Data, elem):
    heap, index = H
    curr = index[elem]
    while curr:
        parent = (curr - 1)//2
        if Data[heap[curr]] < Data[heap[parent]]:
            heap[curr], heap[parent] = heap[parent], heap[curr]
            index[heap[curr]] = curr
        else:
            break
        curr = parent
    index[heap[curr]] = curr
