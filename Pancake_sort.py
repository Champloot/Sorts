from random import randint


def pancake_sort(arr):
    length = len(arr)
    while length > 1:
        ind_max_elem = arr.index(max(arr[:length]))
        arr = arr[ind_max_elem::-1] + arr[ind_max_elem+1:len(arr)]
        arr = arr[length-1::-1] + arr[length:len(arr)]
        length -= 1

    return arr


arr = [randint(-30, 30) for _ in range(20)]

print(arr)
print(pancake_sort(arr))

