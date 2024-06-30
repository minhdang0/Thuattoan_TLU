# from collections import deque

# def minSteptoReachTarget (knghitPos, targetPos):
#     dx = [-1,-2, 1, 2,-1,-2, 2, 1]
#     dy = [-2,-1,-2,-1, 2, 1, 1, 2]
#     queue = deque()
#     visited = set()
    
#     queue.append((knghitPos[0],knghitPos[1],0))
#     visited.add(knghitPos[0],knghitPos[1])
#     while queue:
#         x, y, dis = queue.popleft
        
#         if (x , y) == (targetPos[0] , targetPos[1]):
#             return dis
        
#         for i in range (8):
#             newX, newY = x+dx[i], y+dy[i]
            
#             if (newX,newY ) not in visited :
#                 queue.append((newX,newY,dis+1))
#                 visited.add((newX,newY))
#     return -1

# dfs 
# def dfs (graph , vertex, visited = None) :
#     if visited is None :
#         visited = set()
#     visited.add(vertex)
#     print(vertex, end=" ")
#     for neighbor in graph[vertex]:
#         if neighbor not in visited :
#             dfs(graph, neighbor,visited)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H', 'I'],
#     'F': [],
#     'G': [],
#     'H': [],
#     'I': []
# }

# # Gọi hàm DFS với đỉnh bắt đầu là 'A'
# dfs(graph, 'A')
import heapq
def Dijktra(Graph, Source):
    prev={}
    dist = {}
    Q=[]
    for vertex in Graph:
        dist[vertex] =float('inf')
        prev[vertex]=None
        heapq.heappush(Q,(dist[vertex],vertex))
    dist[Source]=0
    heapq.heappush(Q,(dist[Source],Source))
    while Q:
        current_dist, u = heapq.heappop(Q)
        for v, weight in Graph[u].items():
            alt = dist[u] +weight
            if alt <dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q,(dist[v],v))
    return dist, prev
Graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
Source  ='A'
distance, prev =Dijktra(Graph,Source)
 
 
print('Khoảng cách:', distance)
print('Đường đi:', prev )
        