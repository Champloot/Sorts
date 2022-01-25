from random import randint


def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


arr = [randint(-30, 30) for _ in range(20)]

print(arr)
print(bubble_sort(arr))
