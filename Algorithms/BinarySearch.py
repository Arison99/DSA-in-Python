import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    snapshots = []

    while low <= high:
        mid = (low + high) // 2
        snapshots.append((arr, low, high, mid))
        if arr[mid] == target:
            return mid, snapshots
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, snapshots

# visualization
def visualize_binary_search(snapshots, target):
    for arr, low, high, mid in snapshots:
        plt.bar(range(len(arr)), arr, color='gray')
        plt.bar(low, arr[low], color='blue')
        plt.bar(high, arr[high], color='green')
        plt.bar(mid, arr[mid], color='red' if arr[mid] == target else 'yellow')
        plt.pause(0.5)
        plt.clf()

arr = sorted(np.random.randint(0, 100, 15))
target = arr[np.random.randint(0, len(arr))]
_, snapshots = binary_search(arr, target)

plt.figure(figsize=(10, 5))
visualize_binary_search(snapshots, target)
plt.show()