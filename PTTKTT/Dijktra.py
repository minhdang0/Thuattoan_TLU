import heapq
def Dijkstra (Graph, source):
    dist = {}
    prev = {}
    Q = []
    for vertex in Graph:
        dist[vertex]=float('inf')
        prev[vertex]= None
        heapq.heappush(Q,(dist[vertex],vertex))#add kc từ nguồn đến đỉnh vào queue
    dist[source]=0
    heapq.heappush(Q,(dist[source],source))
    while Q:
        cureent_dist,u =heapq.heappop(Q)
        for v, weight in Graph[u].items():
            alt=dist[u]+weight
            if alt <dist[v]:
                dist[v]=alt
                prev[v]=u
                heapq.heappush(Q,(dist[v],v))
    return dist, prev
Graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
Source  ='A'
distance, prev =Dijkstra(Graph,Source)
 
 
print('Khoảng cách:', distance)
print('Đường đi:', prev )