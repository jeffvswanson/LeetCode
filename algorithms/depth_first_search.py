"""
Reference for depth first search graph traversal algorithm

DFS(graph, node):
    # Input processing work
    node.visited = True
    for neighbor in G[node]:
        if not neighbor.visited:
            DFS(graph, neighbor)
            # Output processing work
"""

def find_path(graph, *, start: int, end: int, path: list = [], visited: set = set()):
    path.append(start)
    visited.add(start)
    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = find_path(graph, start=neighbor, end=end, path=path, visited=visited)
            if result:
                return result
    path.pop()

    



if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    }

    path = find_path(graph, start=0, end=4)
    print(path)
