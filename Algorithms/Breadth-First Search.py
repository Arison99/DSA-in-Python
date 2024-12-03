import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on the given graph starting from the start node.
    
    Parameters:
    graph (networkx.Graph): The graph on which BFS is to be performed.
    start (int): The starting node for BFS.
    
    Returns:
    list: A list of sets, where each set contains the nodes visited up to that point in the BFS.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue to manage the BFS process
    snapshots = []  # List to store snapshots of visited nodes at each step
    
    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            snapshots.append(visited.copy())  # Take a snapshot of the current state of visited nodes
            # Enqueue all unvisited neighbors of the current node
            queue.extend([neighbor for neighbor in graph.neighbors(node) if neighbor not in visited])
    
    return snapshots

def visualize_bfs(graph, snapshots):
    """
    Visualize the BFS process on the given graph using matplotlib.
    
    Parameters:
    graph (networkx.Graph): The graph to be visualized.
    snapshots (list): A list of sets, where each set contains the nodes visited up to that point in the BFS.
    """
    pos = nx.spring_layout(graph)  # Compute the layout for the graph visualization
    
    for visited in snapshots:
        # Draw the graph with nodes colored based on whether they have been visited
        nx.draw(graph, pos, with_labels=True, node_color=['green' if node in visited else 'lightblue' for node in graph.nodes])
        plt.pause(1)  # Pause to create an animation effect
        plt.clf()  # Clear the current figure

# Create a graph and add edges
graph = nx.Graph()
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), 
    (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13),
    (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19),
    (10, 20), (10, 21), (11, 22), (11, 23), (12, 24), (12, 25)
]
graph.add_edges_from(edges)

# Perform BFS and visualize the process
snapshots = bfs(graph, start=1)
plt.figure(figsize=(8, 6))
visualize_bfs(graph, snapshots)