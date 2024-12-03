import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from the start node to all other nodes in the graph.

    Parameters:
    graph (networkx.Graph): The graph on which to run Dijkstra's algorithm.
    start (node): The starting node for Dijkstra's algorithm.

    Returns:
    dict: A dictionary where keys are nodes and values are the shortest distance from the start node.
    """
    # Initialize distances from start node to all other nodes as infinity
    current_distance = {node: float('inf') for node in graph.nodes()}
    current_distance[start] = 0  # Distance to the start node is 0
    visited = {}  # Dictionary to keep track of visited nodes and their distances
    priority_queue = [(0, start)]  # Priority queue to select the node with the smallest distance

    while priority_queue:
        # Pop the node with the smallest distance
        (dist, current_node) = heapq.heappop(priority_queue)
        if current_node in visited:
            continue  # Skip if the node has already been visited
        visited[current_node] = dist  # Mark the node as visited

        # Update distances to neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = dist + weight['weight']
            if neighbor not in visited or distance < current_distance[neighbor]:
                current_distance[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Push the updated distance to the priority queue

    return visited

def visualize_graph(graph, visited):
    """
    Visualizes the graph and highlights the shortest paths found by Dijkstra's algorithm.

    Parameters:
    graph (networkx.Graph): The graph to visualize.
    visited (dict): A dictionary where keys are nodes and values are the shortest distance from the start node.
    """
    pos = nx.spring_layout(graph)  # Position nodes using the spring layout algorithm
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')  # Draw the graph
    # Highlight the edges that are part of the shortest path
    path_edges = [(u, v) for u, v in graph.edges() if visited.get(u) and visited.get(v)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)  # Draw the shortest path edges in red
    plt.show()  # Display the plot

# Create a graph and add weighted edges
graph = nx.Graph()
edges = [(1, 2, 1), (1, 3, 4), (2, 3, 2), (3, 4, 3)]
graph.add_weighted_edges_from(edges)

# Run Dijkstra's algorithm from the start node 1
visited = dijkstra(graph, start=1)

# Visualize the graph and the shortest paths
plt.figure(figsize=(8, 6))
visualize_graph(graph, visited)