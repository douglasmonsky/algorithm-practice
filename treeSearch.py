# Depth-First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_item in graph[start] - visited:
        dfs(graph, next_item, visited)
    return visited


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next_item in graph[start] - set(path):
        yield from dfs_paths(graph, next_item, goal, path + [next_item])


# Breath-First Search
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_item in graph[vertex] - set(path):
            if next_item == goal:
                yield path + [next_item]
            else:
                queue.append((next_item, path + [next_item]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    dfs(graph, 'A')
    list(dfs_paths(graph, 'C', 'F'))

    bfs(graph, 'A')
    list(bfs_paths(graph, 'A', 'F'))

    shortest_path(graph, 'A', 'F')
