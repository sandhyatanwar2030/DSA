def quick_sor(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sor(left) + middle + quick_sor(right)

#OR

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sor(arr)
    print("Sorted array:", sorted_arr)
#or
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)  


# Time Complexity: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always chosen as the pivot).
# Space Complexity:  O(n) 