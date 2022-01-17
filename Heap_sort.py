from random import randint


def heapify(arr, top, array_length):
    largest = top
    left_child = 2*top+1
    right_child = 2*top+2

    if left_child < array_length and arr[left_child] > arr[top]:
        largest = left_child
    if right_child < array_length and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != top:
        arr[largest], arr[top] = arr[top], arr[largest]
        heapify(arr, largest, array_length)


def heap_sort(arr):
    array_length = len(arr)

    for top in range(array_length//2, -1, -1):
        heapify(arr, top, array_length)

    for i in range(array_length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr


arr = []
for _ in range(20):
    arr.append(randint(-30, 30))

print(arr)
print(heap_sort(arr))

