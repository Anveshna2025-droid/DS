def merge_sort(arr):
    # Base case: if the list has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Find the middle and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. CONQUER: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. COMBINE: Merge the sorted halves back together
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both lists and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_result = merge_sort(my_list)
print(f"Sorted list: {sorted_result}")