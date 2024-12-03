import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    current_distance = {node: float('inf') for node in graph.nodes()}
    current_distance[start] = 0
    visited = {}
    priority_queue = [(0, start)]

    while priority_queue:
        (dist, current_node) = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited[current_node] = dist

        for neighbor, weight in graph[current_node].items():
            distance = dist + weight['weight']
            if neighbor not in visited or distance < current_distance[neighbor]:
                current_distance[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return visited

def visualize_graph(graph, visited):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    path_edges = [(u, v) for u, v in graph.edges() if visited.get(u) and visited.get(v)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.show()

graph = nx.Graph()
edges = [(1, 2, 1), (1, 3, 4), (2, 3, 2), (3, 4, 3)]
graph.add_weighted_edges_from(edges)

visited = dijkstra(graph, start=1)
plt.figure(figsize=(8, 6))
visualize_graph(graph, visited)