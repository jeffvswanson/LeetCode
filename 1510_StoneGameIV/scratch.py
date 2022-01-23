from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def recursive_dfs(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.recursive_dfs(neighbor, visited)

    def iterative_dfs(self, v):
        print(f"iterative DFS starting from vertex {v}")
        visited = set()
        not_visited = [v]
        while not_visited:
            vertex = not_visited.pop()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        not_visited.append(neighbor)
        print()
    
    def dfs(self, v):
        print(f"recursive DFS starting from vertex {v}")
        visited = set()

        self.recursive_dfs(v, visited)
        print()

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


g.dfs(2)
g.iterative_dfs(2)
