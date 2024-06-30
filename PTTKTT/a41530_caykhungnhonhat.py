class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal_mst(graph):
    mst = []
    edges = sorted(graph, key=lambda edge: edge[0])
    dsu = DSU(len(set([v for edge in graph for v in edge[1:]])))

    for weight, start, end in edges:
        if dsu.find(start) != dsu.find(end):
            mst.append((weight, start, end))
            dsu.union(start, end)

    return mst

graph = [
    (1, 0, 1),
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3)
]

mst = kruskal_mst(graph)
print("Các cạnh trong Cây bao trùm tối thiểu (MST):")
for weight, start, end in mst:
    print(f"Cạnh từ {start} đến {end} có trọng số {weight}")
