from collections import deque

def MaxFlow(G):
    # construct residual graph with flow/cap
    Gr = [{} for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            Gr[u][v] = [0, G[u][v]]
            Gr[v][u] = [0, 0]
    # find augmenting path until fails
    total_flow = 0
    sink = len(Gr) - 1
    augmentingPathFound = True
    while augmentingPathFound:
        augmentingPathFound = False
        # BFS
        Prev = [None]*len(Gr)
        Prev[0] = len(Gr)
        Queue = deque([0])
        while Queue:
            u = Queue.popleft()
            for v in Gr[u]:
                flow, cap = Gr[u][v]
                if Prev[v] is None and flow < cap:
                    Prev[v] = u
                    if v == sink:
                        augmentingPathFound = True
                        break
                    Queue.append(v)
            # this helps break two levels of loops
            else:
                continue
            break
        # trace back the path if found
        if augmentingPathFound:
            # find bottleneck
            inc = float("inf")
            curr = sink
            while curr != 0:
                flow, cap = Gr[Prev[curr]][curr]
                room = cap - flow
                if room < inc:
                    inc = room
                curr = Prev[curr]
            # push more flow
            curr = sink
            while curr != 0:
                Gr[Prev[curr]][curr][0] += inc
                Gr[curr][Prev[curr]][0] -= inc
                curr = Prev[curr]
            total_flow += inc
    return Gr, total_flow
