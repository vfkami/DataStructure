# bubble sort goes through the array and swaps between
# array[i] and array[i + 1] if i > i + 1
def bubble_sort(array):    
    for _ in range(len(array)):
        for j in range(len(array) - 1):
            array[j], array[j + 1] = swap(array[j], array[j + 1]) 
                            
    return array

## swap the elements if a > b
def swap(a, b):
    if(a < b):
        return a, b
    return b, a
    
# verify if array is sorted
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sorted_array)
    print(bubble_sort(sorted_array))

    unsorted_array = [4, 6, 3, 1, 2, 9, 8, 5, 7]
    print(unsorted_array)
    print(bubble_sort(unsorted_array))

    worstcase_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(worstcase_array)
    print(bubble_sort(worstcase_array))
    
    