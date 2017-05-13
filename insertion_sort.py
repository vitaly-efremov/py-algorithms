def insertion_sort_v1(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i
        while j > 0 and array[j-1] > x:
            array[j] = array[j-1]
            j -= 1
        array[j] = x
    return array


def insertion_sort_v2(array):
    for i, x in enumerate(array[1:], 1):
        j = i
        while j > 0 and array[j-1] > x:
            array[j] = array[j-1]
            j -= 1
        array[j] = x
    return array


if __name__ == '__main__':
    unordered_list = [2, 3, 1, 5, 0, 8, 9, 7]
    print('Ordered list with V1:', insertion_sort_v1(unordered_list))
    print('Ordered list with V2:', insertion_sort_v2(unordered_list))
