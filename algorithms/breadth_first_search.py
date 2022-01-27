from collections import deque


def bfs_traversal(graph, root):
    q = deque()
    visited = set()
    q.append(root)
    visited.add(root)
    
    while q:
        parent_node = q.pop()
        print(parent_node, end=' ')
        for neighbor in graph[parent_node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    print()


def bfs_connected_nodes(graph, *, start, end):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)

    path = []
    has_path = False
    while q:
        parent = q.pop()
        path.append(parent)
        if parent == end:
            has_path = True
            break
        for neighbor in graph[parent]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    if has_path:
        print(path)
    else:
        print(f"no path between starting node {start} and node {end}")




if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [1, 3, 5],
        3: [1, 2, 4],
        4: [3],
        5: [2],
    }
    bfs_traversal(graph, 1)
    
    graph = {
    1 : [2, 3, 4, 5],
    2 : [1, 3],
    3 : [1, 2, 4, 6],
    4 : [1, 3, 5, 6],
    5 : [1, 4, 6],
    6 : [3, 4, 5],
    7 : [],
    }
    bfs_connected_nodes(graph, start=1, end=6)
    bfs_connected_nodes(graph, start=1, end=7)