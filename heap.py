class Heap(object):
    def __init__(self):
        self.array = []
        self.n = 0

    def insert(self, value):
        self.array.append(value)
        self.n += 1
        child_index = self.n - 1
        parent_index = (child_index - 1) // 2

        while child_index > 0 and self.array[parent_index] < self.array[child_index]:
            self.array[parent_index], self.array[child_index] = self.array[child_index], self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) // 2

    def heapify(self, parent=0):
        while True:
            left_child = 2*parent + 1
            right_child = left_child + 1
            largest_child = parent

            if left_child < self.n and self.array[largest_child] < self.array[left_child]:
                largest_child = left_child
            if right_child < self.n and self.array[largest_child] < self.array[right_child]:
                largest_child = right_child

            if parent != largest_child:
                self.array[parent], self.array[largest_child] = self.array[largest_child], self.array[parent]
                parent = largest_child
            else:
                break

    def pop_max(self):
        last_value = self.array.pop()

        self.n -= 1
        if self.n > 0:
            max_value = self.array[0]
            self.array[0] = last_value
            self.heapify()
            return max_value
        return last_value

    def get_sorted_values(self, reverse=True):
        sorted_array = []
        while self.array:
            sorted_array.append(self.pop_max())

        return sorted_array if reverse else sorted_array[::-1]

if __name__ == '__main__':
    unsorted_array = [1, 2, 0, 5, 3]
    heap = Heap()
    for x in unsorted_array:
        heap.insert(x)

    print(heap.array)