from utils import measured_func


def merge_parts(left_part, right_part):
    merged_list = []

    while left_part or right_part:
        x = left_part[0] if left_part else None
        y = right_part[0] if right_part else None

        if y is None or (x is not None and x < y):
            merged_list.append(x)
            del left_part[0]
        else:
            merged_list.append(y)
            del right_part[0]

    return merged_list


def merge_sort_v1(unordered_list):
    n = len(unordered_list)
    if n <= 1:
        return unordered_list

    middle = n // 2
    left_part = merge_sort_v1(unordered_list[: middle])
    right_part = merge_sort_v1(unordered_list[middle:])

    return merge_parts(left_part, right_part)


def merge_sort_v2(unordered_list):
    n = len(unordered_list)
    ordered_list = []

    if n <= 1:
        return unordered_list

    middle = n // 2
    left_part = merge_sort_v1(unordered_list[: middle])
    right_part = merge_sort_v1(unordered_list[middle:])

    left_inc, right_inc = 0, 0
    while left_inc < len(left_part) and right_inc < len(right_part):
        left_value = left_part[left_inc]
        right_value = right_part[right_inc]

        if left_value < right_value:
            ordered_list.append(left_value)
            left_inc += 1
        else:
            ordered_list.append(right_value)
            right_inc += 1

    ordered_list += left_part[left_inc:]
    ordered_list += right_part[right_inc:]
    return ordered_list


if __name__ == '__main__':
    unordered_list = [2, 3, 1, 5, 0, 8, 9, 7]
    print('Ordered list with V1:', measured_func(merge_sort_v1)(unordered_list))
    print('Ordered list with V2:', measured_func(merge_sort_v2)(unordered_list))
