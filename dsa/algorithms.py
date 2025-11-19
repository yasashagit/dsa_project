# sorting algorithms (Bubble Sort, Insertion Sort, Merge Sort)
# searching algorithms (Linear Search, Binary Search), 

def bubble_sort(arr):
    """Sorts an array using the Bubble Sort algorithm."""
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Or if you define bubble_sort directly in the notebook:
def bubble_sort_a(arr_to_sort): # Renamed parameter to avoid conflict with the list in the animation
    """
    Sorts an array using the Bubble Sort algorithm and yields states for animation.
    This version is modified to yield intermediate states for visualization.
    """
    arr = list(arr_to_sort) # Work on a copy
    n = len(arr)
    for i in range(n):
        swapped = False # Optimization: if no two elements were swapped by one pass, then the array is sorted
        for j in range(0, n - i - 1):
            # Yield current state BEFORE comparison for visualization
            yield list(arr), j, j + 1, "comparing" # Current elements being compared
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                # Yield current state AFTER swap for visualization
                yield list(arr), j, j + 1, "swapping" # Elements just swapped
        
        # After each pass, the last i elements are sorted.
        # Yield the state with the element fixed.
        yield list(arr), -1, n - i - 1, "sorted_fixed" # n-i-1 is the index of the element just placed
        
        if not swapped:
            # If no swaps occurred in this pass, the array is sorted.
            break
            
    yield list(arr), -1, -1, "finished" # Indicate final state
def insertion_sort(arr):
    """Sorts an array using the Insertion Sort algorithm."""
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm."""
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into two halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Recursively sort the first and second halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking for any remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr