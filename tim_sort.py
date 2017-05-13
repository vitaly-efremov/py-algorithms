from insertion_sort import insertion_sort_v1
from merge_sort import merge_parts


def get_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def tim_sort(array):
    def cmp(a, b):
        return (a > b) - (a < b)

    n = len(array)
    if n < 2:
        return array

    min_run = get_min_run(n)

    runs = []
    run_start = 0
    while run_start < n:
        run_len = 2
        cmp_sign = cmp(array[run_start], array[run_start+1])
        for run_i in range(run_start+1, n-1):
            if cmp(array[run_i], array[run_i+1]) == cmp_sign:
                run_len += 1
            else:
                break

        if run_len < min_run:
            run_len += min_run - run_len

        run_end = run_start + run_len
        if run_end > n:
            run_len -= run_end - n

        runs.append((run_start, run_start + run_len))
        run_start = run_end

    sorted_stack = []
    for run_start, run_len in runs:
        run_array = array[run_start: run_len]
        insertion_sort_v1(run_array)
        sorted_stack.append(run_array)

    run_x = []
    while sorted_stack:
        run_x = sorted_stack.pop()

        if not sorted_stack:
            return run_x

        run_y = sorted_stack.pop()
        sorted_stack.append(merge_parts(run_x, run_y))

    return run_x

if __name__ == '__main__':
    from random import shuffle
    unordered_list = [2, 3, 1, 5, 0, 8, 9, 7, 4, 6, 12, 11, 76, 81, 17]*5
    print('Array len =', len(unordered_list))
    shuffle(unordered_list)
    print('Ordered list with V1:', tim_sort(unordered_list))