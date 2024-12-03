import matplotlib.pyplot as plt
import numpy as np
import time

def bubbleSort(arr):
    n = len(arr)
    snapshots = [arr.copy()]
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                snapshots.append(arr.copy())
    return snapshots

# visualization
def visualize_bubble_sort(snapshots):
    for arr in snapshots:
        plt.bar(range(len(arr)), arr, color='skyblue')
        plt.pause(0.2)
        plt.clf()

arr = np.random.randint(1, 50, 10)
snapshots = bubbleSort(arr)

plt.figure(figsize=(10, 5))
visualize_bubble_sort(snapshots)
plt.show()
