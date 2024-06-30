from collections import deque

def BFS (graph, start_vertex):
    
    visited = set()
    queue = deque([start_vertex])
    while queue:
        vertex= queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            for neighbor in  graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Gọi hàm BFS với đỉnh bắt đầu là 'A'
BFS(graph, 'A')
