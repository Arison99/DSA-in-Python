import matplotlib.pyplot as plt
import numpy as np
import time

def bubbleSort(arr):
    """
    Perform bubble sort on the given array and capture snapshots of the array at each step.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A list of snapshots of the array at each step of the sorting process.
    """
    n = len(arr)
    snapshots = [arr.copy()]  # Initialize the list of snapshots with the initial array
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                snapshots.append(arr.copy())  # Capture the snapshot after each swap
    return snapshots

def visualize_bubble_sort(snapshots):
    """
    Visualize the bubble sort process using bar charts.
    
    Parameters:
    snapshots (list): A list of snapshots of the array at each step of the sorting process.
    """
    for arr in snapshots:
        plt.bar(range(len(arr)), arr, color='skyblue')  # Create a bar chart for the current snapshot
        plt.pause(0.2)  # Pause to create an animation effect
        plt.clf()  # Clear the current figure

# Generate a random array of integers
arr = np.random.randint(1, 50, 10)

# Perform bubble sort and capture snapshots
snapshots = bubbleSort(arr)

# Set up the plot
plt.figure(figsize=(10, 5))

# Visualize the sorting process
visualize_bubble_sort(snapshots)

# Display the plot
plt.show()
