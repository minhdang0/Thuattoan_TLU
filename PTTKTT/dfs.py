def dfs (graph , vertex, visited = None) :
    if visited is None :
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited :
            dfs(graph, neighbor,visited)
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

# Gọi hàm DFS với đỉnh bắt đầu là 'A'
dfs(graph, 'A')
            