from random import randint


def radix_sort(arr):
    values = 10
    length = len(str(max(arr)))
    for i in range(length):
        time_arr = [[] for _ in range(values)]
        for elem in arr:
            elem_digit = elem // 10**i % 10
            time_arr[elem_digit].append(elem)
        arr = []
        for i in range(values):
            arr += time_arr[i]

    return arr


arr = []
for _ in range(20):
    arr.append(randint(0, 60))

print(arr)
print(radix_sort(arr))

