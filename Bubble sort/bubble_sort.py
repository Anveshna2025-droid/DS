def bubble_sort(data):
    n = len(data)
    
    # Outer loop: goes through the entire list n times
    for i in range(n):
        swapped = False
        
        # Inner loop: compares adjacent elements
        # We subtract 'i' because the last 'i' elements are already sorted
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Swap the elements
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        # Optimization: If no two elements were swapped, the list is sorted
        if not swapped:
            break
            
    return data

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)

print(f"Sorted list: {sorted_list}")