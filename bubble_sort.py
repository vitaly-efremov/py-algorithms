def bubble_sort(array):
    while True:
        is_sorted = True
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                is_sorted = False
        if is_sorted:
            return array


if __name__ == '__main__':
    unordered_list = [2, 3, 1, 5, 0, 8, 9, 7]
    print('Ordered list with V1:', bubble_sort(unordered_list))
