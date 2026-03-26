def counting_sort(arr):
    # Return an empty list if input is empty
    if not arr:
        return []
    
    # 1. Find the range of input values
    min_val = min(arr)
    max_val = max(arr)
    
    # 2. Initialize the counting array
    count_range = max_val - min_val + 1
    count = [0] * count_range
    
    # 3. Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    
    # 4. Compute the prefix sums to determine positions
    for i in range(1, count_range):
        count[i] += count[i - 1]
    
    # 5. Build the output array (stable sort)
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num
    
    return output


# Example usage
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    sorted_data = counting_sort(data)
    print("Original array:", data)
    print("Sorted array:  ", sorted_data)