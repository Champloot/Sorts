from random import randint


def shaker_sort(arr):
    length = len(arr)
    start = 0
    end = length-1
    need_swap = True

    while need_swap:
        need_swap = True
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                need_swap = True
        end -= 1

        if not(need_swap):
            break

        need_swap = False
        for i in range(end, start, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                need_swap = True
        start += 1

    return arr


arr = [randint(-30, 30) for _ in range(20)]

print(arr)
print(shaker_sort(arr))

