import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the target value.
    
    Parameters:
    arr (list): A sorted list of elements to search.
    target (int): The value to search for in the array.
    
    Returns:
    int: The index of the target value if found, otherwise -1.
    list: A list of snapshots showing the state of the array during each step of the search.
    """
    low, high = 0, len(arr) - 1
    snapshots = []

    while low <= high:
        mid = (low + high) // 2
        snapshots.append((arr.copy(), low, high, mid))  # Store the current state of the array and pointers
        if arr[mid] == target:
            return mid, snapshots
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, snapshots

def visualize_binary_search(snapshots, target):
    """
    Visualize the binary search process using bar charts.
    
    Parameters:
    snapshots (list): A list of snapshots showing the state of the array during each step of the search.
    target (int): The value being searched for.
    """
    for arr, low, high, mid in snapshots:
        plt.bar(range(len(arr)), arr, color='gray')  # Plot the array elements as gray bars
        plt.bar(low, arr[low], color='blue')  # Highlight the low pointer as a blue bar
        plt.bar(high, arr[high], color='green')  # Highlight the high pointer as a green bar
        plt.bar(mid, arr[mid], color='red' if arr[mid] == target else 'yellow')  # Highlight the mid pointer
        plt.pause(0.5)  # Pause to create an animation effect
        plt.clf()  # Clear the plot for the next step

# Generate a sorted array of random integers
arr = sorted(np.random.randint(0, 100, 15))
# Select a random target value from the array
target = arr[np.random.randint(0, len(arr))]
# Perform binary search and get the snapshots
_, snapshots = binary_search(arr, target)

# Set up the plot
plt.figure(figsize=(10, 5))
# Visualize the binary search process
visualize_binary_search(snapshots, target)
# Display the plot
plt.show()