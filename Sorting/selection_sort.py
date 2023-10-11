import sys

def selection_sort(array):
    for i in range(len(array)):
        index = 0
        value = sys.maxsize
        for j in range(i, len(array)):
            if(array[j] < value):
                index = j
                value = array[j]
                
        key = array[i]
        array[i] = array[index]     
        array[index] = key
    
    return array

# verify if array is sorted
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sorted_array)
    print(selection_sort(sorted_array))

    unsorted_array = [4, 6, 3, 1, 2, 9, 8, 5, 7]
    print(unsorted_array)
    print(selection_sort(unsorted_array))

    worstcase_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(worstcase_array)
    print(selection_sort(worstcase_array))