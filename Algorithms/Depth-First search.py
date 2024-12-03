import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def dfs(graph, start, visited=None, snapshots=None):
    """
    Perform Depth First Search (DFS) on a graph starting from a given node.

    Parameters:
    graph (networkx.Graph): The graph to perform DFS on.
    start (int): The starting node for DFS.
    visited (list, optional): List to keep track of visited nodes.
    snapshots (list, optional): List to store snapshots of the visited nodes at each step.

    Returns:
    list: A list of snapshots showing the visited nodes at each step.
    """
    if visited is None:
        visited = []
        snapshots = []
    visited.append(start)
    snapshots.append(visited.copy())
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, snapshots)
    return snapshots

def visualize_dfs(graph, snapshots):
    """
    Visualize the DFS process on a graph using matplotlib.

    Parameters:
    graph (networkx.Graph): The graph to visualize.
    snapshots (list): List of snapshots showing the visited nodes at each step.
    """
    pos = nx.spring_layout(graph)  # Position nodes using the spring layout algorithm
    for visited in snapshots:
        # Draw the graph with nodes colored based on whether they have been visited
        nx.draw(graph, pos, with_labels=True, node_color=['green' if node in visited else 'lightblue' for node in graph.nodes])
        plt.pause(1)  # Pause to create an animation effect
        plt.clf()  # Clear the figure for the next snapshot

# Create an empty graph
graph = nx.Graph()

# Define the edges of the graph
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), 
    (6, 12), (6, 13), (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19), (10, 20), 
    (10, 21), (11, 22), (11, 23), (12, 24), (12, 25), (13, 26), (13, 27), (14, 28), 
    (14, 29), (15, 30)
]

# Add edges to the graph
graph.add_edges_from(edges)

# Perform DFS starting from node 1 and get the snapshots
snapshots = dfs(graph, start=1)

# Set the figure size for the plot
plt.figure(figsize=(10, 8))

# Visualize the DFS process
visualize_dfs(graph, snapshots)