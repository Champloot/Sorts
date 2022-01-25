from random import randint


def heapify(arr, top, length):
    largest = top
    left_child = 2*top+1
    right_child = 2*top+2

    if left_child < length and arr[left_child] > arr[top]:
        largest = left_child
    if right_child < length and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != top:
        arr[largest], arr[top] = arr[top], arr[largest]
        heapify(arr, largest, length)


def heap_sort(arr):
    length = len(arr)

    for top in range(length//2, -1, -1):
        heapify(arr, top, length)

    for i in range(length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr


arr = [randint(-30, 30) for _ in range(20)]

print(arr)
print(heap_sort(arr))

