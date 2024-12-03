import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def visualize_kmeans(data, n_clusters):
    """
    Visualize K-Means clustering on a 2D dataset.

    Parameters:
    data (numpy.ndarray): The input data to cluster, should be a 2D array.
    n_clusters (int): The number of clusters to form.

    This function performs K-Means clustering on the input data and plots the clusters
    along with their centroids.
    """
    # Initialize the KMeans object with the number of clusters and a random state for reproducibility
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    
    # Fit the KMeans model to the data
    kmeans.fit(data)
    
    # Get the labels assigned to each data point
    labels = kmeans.labels_
    
    # Get the coordinates of the cluster centroids
    centroids = kmeans.cluster_centers_

    # Plot each cluster with a different color
    for i in range(n_clusters):
        # Select the points that belong to the current cluster
        cluster_points = data[labels == i]
        # Scatter plot of the cluster points
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i+1}')
    
    # Plot the centroids of the clusters
    plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='x', label='Centroids')
    
    # Add a legend to the plot
    plt.legend()
    
    # Display the plot
    plt.show()

# Generate random data points for clustering
data = np.random.rand(100, 2) * 10

# Define the number of clusters
n_clusters = 3

# Set the size of the plot
plt.figure(figsize=(8, 6))

# Call the function to visualize K-Means clustering
visualize_kmeans(data, n_clusters)