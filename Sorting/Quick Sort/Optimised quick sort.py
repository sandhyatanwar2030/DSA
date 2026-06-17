def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)


# Time Complexity: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always chosen as the pivot).
# Space Complexity: O(log n)