def Merge_Sort(arr):
#base condition
    if len(arr) > 1: 
        mid = len(arr) // 2

        L = arr[:mid]   #left Array
        R = arr[mid:]   #Right Array
#RECURSIVE CALL
        Merge_Sort(L)
        Merge_Sort(R)
#initialise pointers for L, R and arr
        i = j = k = 0

        while i < len(L) and j < len(R):   #this loop run till left and and right both have elements in arrays
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1         
            else:
                arr[k] = R[j]
                j += 1
            k += 1

#copy remaining elements of L[] if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

#copy remaining elements of R[] if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



arr = list(map(int, input("Enter the elements of the array separated by space:").split()))   
Merge_Sort(arr)
print("Sorted array is:", arr)

