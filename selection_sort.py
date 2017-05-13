def selection_sort_v1(array):
    n = len(array)
    for i in range(n):
        min_j = i
        for j in range(i+1, n):
            if array[j] < array[min_j]:
                min_j = j

        if min_j != i:
            array[i], array[min_j] = array[min_j], array[i]
    return array


def selection_sort_v2(array):
    for i in range(len(array)-1, 0, -1):
        min_j = 0
        for j in range(1, i+1):
            if array[j] > array[min_j]:
                min_j = j

        array[i], array[min_j] = array[min_j], array[i]
    return array

if __name__ == '__main__':
    unordered_list = [1, 4, 0, 1, 2, 6, 9]
    print('Ordered list with V1:', selection_sort_v1(unordered_list))
    print('Ordered list with V1:', selection_sort_v2(unordered_list))