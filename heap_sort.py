from heap import Heap


def heap_sort(array, reverse=False):
    sorted_array = []
    heap = Heap()
    for x in array:
        heap.insert(x)
    print(heap.array)

    while heap.array:
        sorted_array.append(heap.pop_max())

    return sorted_array if reverse else sorted_array[::-1]

if __name__ == '__main__':
    unordered_list = [2, 3, 1, 5, 0, 8, 9, 7]
    print('Ordered list with V1:', heap_sort(unordered_list))
