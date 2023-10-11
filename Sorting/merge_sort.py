def split_list(array):
    half = len(array)//2
    return array[:half], array[half:]

def merge_sort(array):
    if(len(array) == 1):
        return array
    
    f, s = split_list(array)
    f = merge_sort(f)
    s = merge_sort(s)
        
    return merge(s, f)

def merge(a, b):
    c = []
    while a and b:
        if(a[0] < b[0]):
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    
    while a:
        c.append(a[0])
        a.pop(0)
                    
    while b:
        c.append(b[0])
        b.pop(0)              
    return c

if __name__ == "__main__":
    unsorted_array = [9, 5, 4, 3, 7, 2, 8, 1, 6]
    print(unsorted_array)
    print(merge_sort(unsorted_array))

    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sorted_array)
    print(merge_sort(sorted_array))

    worstcase_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(worstcase_array)
    print(merge_sort(worstcase_array))
    