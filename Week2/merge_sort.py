def mergesort(array):
    if len(array) <= 1:
        return array
    mid = (len(array))//2
    left_subarray = array[:mid]
    right_subarray = array[mid:]

    left_subarray = mergesort(left_subarray)
    right_subarray = mergesort(right_subarray)
    
    sorted_array = []
    left_index = right_index = 0
    while left_index < len(left_subarray) and right_index < len(right_subarray):
        if left_subarray[left_index] < right_subarray[right_index]:
            sorted_array.append(left_subarray[left_index])
            left_index += 1
        else:
            sorted_array.append(right_subarray[right_index])
            right_index += 1
    sorted_array.extend(left_subarray[left_index:])
    sorted_array.extend(right_subarray[right_index:])
    return sorted_array
input_list = list(map(int, input().split()))
result = mergesort(input_list)
print(result)