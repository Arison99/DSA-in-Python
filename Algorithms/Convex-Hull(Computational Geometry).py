import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

def visualize_convex_hull(points):
    """
    Visualize the convex hull of a set of 2D points.

    Parameters:
    points (ndarray): An array of shape (n, 2) representing n points in 2D space.
    """
    # Compute the convex hull of the points
    hull = ConvexHull(points)
    
    # Scatter plot of the points
    plt.scatter(points[:,0], points[:,1])
    
    # Plot the edges of the convex hull
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'r-')
    
    # Display the plot
    plt.show()

# Generate 10 random points in 2D space, scaled by 10
points = np.random.rand(10, 2) * 10

# Set the size of the plot
plt.figure(figsize=(8, 6))

# Visualize the convex hull of the generated points
visualize_convex_hull(points)