def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    queue = [[x] for x in arr]
    while len(queue) > 1:
        new_queue = []
        for i in range(0, len(queue), 2):
            if i + 1 < len(queue):
                new_queue.append(merge(queue[i], queue[i + 1]))
            else:
                new_queue.append(queue[i])
        queue = new_queue

    return queue[0]

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
