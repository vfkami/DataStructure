def insertion_sort(array):
    ## starts at index 1
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        ## moves backward i -> 0
        while j >= 0 and key < array[j] :
            # moves elements j to j-1 that are
            # greater than key and put key in
            # last position
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sorted_array)
    print(insertion_sort(sorted_array))

    unsorted_array = [9, 5, 4, 3, 7, 2, 8, 1, 6]
    print(unsorted_array)
    print(insertion_sort(unsorted_array))

    worstcase_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(worstcase_array)
    print(insertion_sort(worstcase_array))
    