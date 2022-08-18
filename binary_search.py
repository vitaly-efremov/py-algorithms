def binary_search(items, element):
	start_index = 0
	end_index = len(items) - 1

	while start_index <= end_index:
		mid_index = (start_index + end_index) // 2
		value = items[mid_index]
		if value == element:
			return mid_index
		if value > element:
			end_index = mid_index - 1
		else:
			start_index = mid_index + 1
	return -1


assert binary_search([0, 1, 2, 3], 2) == 2
assert binary_search([], 2) == -1
assert binary_search([1, 2], 3) == -1
assert binary_search([1, 2, 6, 6, 9], 6) == 2
