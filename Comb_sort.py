from random import randint


def comb_sort(arr):
    length = len(arr)
    dist = length
    need_swap = True
    while dist > 1 or need_swap:
        need_swap = False
        dist = max(1, int(dist // 1.247))
        for i in range(length - dist):
            j = i + dist
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                need_swap = True
    return arr


arr = []
for _ in range(20):
    arr.append(randint(-30, 30))

print(arr)
print(comb_sort(arr))

