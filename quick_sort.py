from utils import measured_func


def quick_sort_classic(array, start_i=0, last_i=None):
    if last_i is None:
        last_i = len(array) - 1

    if start_i >= last_i:
        return array

    median = array[(last_i + start_i) // 2]

    left_i, right_i = start_i, last_i

    while right_i > left_i:
        while array[left_i] < median:
            left_i += 1

        while array[right_i] > median:
            right_i -= 1

        if left_i <= right_i:
            if array[right_i] < array[left_i]:
                array[left_i], array[right_i] = array[right_i], array[left_i]
            left_i += 1
            right_i -= 1

    if start_i < right_i:
        quick_sort_classic(array, start_i, right_i)
    if last_i > left_i:
        quick_sort_classic(array, left_i, last_i)

    return array


def quick_sort(array):
    if len(array) < 2:
        return array

    less = []
    equals = []
    greater = []
    pivot = array[0]

    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equals.append(element)

    return quick_sort(less) + equals + quick_sort(greater)


def quick_sort_short(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    return quick_sort([x for x in array if x < pivot]) + quick_sort([x for x in array if x >= pivot])


if __name__ == '__main__':
    unordered_list = [4, 9, 7, 6, 2, 3, 8]
    print('Ordered list with V1:', measured_func(quick_sort_classic)(unordered_list))
    print('Ordered list with V2:', measured_func(quick_sort)(unordered_list))
    print('Ordered list with V3:', measured_func(quick_sort_short)(unordered_list))

