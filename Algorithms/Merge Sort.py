import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    snapshots = []
    def merge_sort_recursive(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort_recursive(arr, left, mid)
        merge_sort_recursive(arr, mid + 1, right)
        merge(arr, left, mid, right)
        snapshots.append(arr.copy())

    def merge(arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        temp.extend(arr[i:mid + 1])
        temp.extend(arr[j:right + 1])
        arr[left:right + 1] = temp

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return snapshots

# visualization
def visualize_merge_sort(snapshots):
    for arr in snapshots:
        plt.bar(range(len(arr)), arr, color='skyblue')
        plt.pause(0.5)
        plt.clf()

arr = np.random.randint(1, 50, 10)
snapshots = merge_sort(arr)

plt.figure(figsize=(10, 5))
visualize_merge_sort(snapshots)
plt.show()
