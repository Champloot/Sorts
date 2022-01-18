from random import randint


def shaker_sort(arr):
    array_length = len(arr)
    start = 0
    end = array_length-1
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


arr = []
for _ in range(20):
    arr.append(randint(-30, 30))

print(arr)
print(shaker_sort(arr))

