from collections import deque

# Dinic's algorithm (Ford–Fulkerson with a level graph)
def Dinic(G, s, t):
    n = len(G)
    # construct residual graph with flow/cap
    Gr = [{} for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            Gr[u][v] = [0, G[u][v]]
            if u not in Gr[v]: # do not overwrite existing edges
                Gr[v][u] = [0, 0]
    # find augmenting path until fails
    total_flow = 0
    augmenting_path_found = True
    while augmenting_path_found:
        # build the level graph with BFS
        Level = [-1]*n # distance to source in number of edges
        Level[s] = 0
        BFS_Queue = deque([s])
        while BFS_Queue:
            u = BFS_Queue.popleft()
            for v in Gr[u]:
                flow, cap = Gr[u][v]
                if Level[v] == -1 and flow < cap:
                    Level[v] = Level[u] + 1
                    BFS_Queue.append(v)
        augmenting_path_found = Level[t] != -1
        if augmenting_path_found:
            # send flow along all path with DFS
            more_flow = True
            while more_flow:
                more_flow = _send_flow(Gr, Level, float("inf"), s, t)
                total_flow += more_flow
    return Gr, total_flow

def _send_flow(Gr, Level, input_flow, u, t):
    if u == t:
        return input_flow
    total_output_flow = 0
    for v in Gr[u]:
        flow, cap = Gr[u][v]
        # the level graph creates a DAG
        if Level[v] == Level[u] + 1 and flow < cap:
            output_flow = input_flow
            # find bottleneck
            room = cap - flow
            if room < output_flow:
                output_flow = room
            output_flow = _send_flow(Gr, Level, output_flow, v, t)
            if output_flow:
                Gr[u][v][0] += output_flow
                Gr[v][u][0] -= output_flow
                total_output_flow += output_flow
                input_flow -= output_flow
    return total_output_flow
