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
