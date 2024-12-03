import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    """
    Perform merge sort on the given array and capture snapshots of the array at each merge step.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A list of snapshots of the array at each merge step.
    """
    snapshots = []

    def merge_sort_recursive(arr, left, right):
        """
        Recursively divide the array into halves and merge them in sorted order.

        Parameters:
        arr (list): The list of elements to be sorted.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
        """
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort_recursive(arr, left, mid)  # Sort the first half
        merge_sort_recursive(arr, mid + 1, right)  # Sort the second half
        merge(arr, left, mid, right)  # Merge the sorted halves
        snapshots.append(arr.copy())  # Capture the snapshot after each merge

    def merge(arr, left, mid, right):
        """
        Merge two sorted subarrays into a single sorted subarray.

        Parameters:
        arr (list): The list of elements to be sorted.
        left (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        right (int): The ending index of the second subarray.
        """
        temp = []
        i, j = left, mid + 1
        # Merge the two subarrays into temp
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        # Append remaining elements of the first subarray, if any
        temp.extend(arr[i:mid + 1])
        # Append remaining elements of the second subarray, if any
        temp.extend(arr[j:right + 1])
        # Copy the merged elements back to the original array
        arr[left:right + 1] = temp

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return snapshots

# visualization
def visualize_merge_sort(snapshots):
    """
    Visualize the merge sort process using bar charts.

    Parameters:
    snapshots (list): A list of snapshots of the array at each merge step.
    """
    for arr in snapshots:
        plt.bar(range(len(arr)), arr, color='skyblue')
        plt.pause(0.5)  # Pause to create an animation effect
        plt.clf()  # Clear the current figure

# Generate a random array of integers
arr = np.random.randint(1, 50, 10)
# Perform merge sort and capture snapshots
snapshots = merge_sort(arr)

# Set up the plot
plt.figure(figsize=(10, 5))
# Visualize the merge sort process
visualize_merge_sort(snapshots)
# Show the final plot
plt.show()
