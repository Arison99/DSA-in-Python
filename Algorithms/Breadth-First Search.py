import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    snapshots = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            snapshots.append(visited.copy())
            queue.extend([neighbor for neighbor in graph.neighbors(node) if neighbor not in visited])
    return snapshots

# visualization
def visualize_bfs(graph, snapshots):
    pos = nx.spring_layout(graph)
    for visited in snapshots:
        nx.draw(graph, pos, with_labels=True, node_color=['green' if node in visited else 'lightblue' for node in graph.nodes])
        plt.pause(1)
        plt.clf()

graph = nx.Graph()
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), 
    (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13),
    (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19),
    (10, 20), (10, 21), (11, 22), (11, 23), (12, 24), (12, 25)
]
graph.add_edges_from(edges)

snapshots = bfs(graph, start=1)
plt.figure(figsize=(8, 6))
visualize_bfs(graph, snapshots)