from random import randint


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        left_ind = 0
        right_ind = 0
        arr_ind = 0
        while len(left) > left_ind and len(right) > right_ind:
            if left[left_ind] < right[right_ind]:
                arr[arr_ind] = left[left_ind]
                left_ind += 1
            else:
                arr[arr_ind] = right[right_ind]
                right_ind += 1
            arr_ind += 1

        while len(left) > left_ind:
            arr[arr_ind] = left[left_ind]
            arr_ind += 1
            left_ind += 1

        while len(right) > right_ind:
            arr[arr_ind] = right[right_ind]
            arr_ind += 1
            right_ind += 1

    return arr


arr = []
for _ in range(20):
    arr.append(randint(-30, 30))

print(arr)
print(merge_sort(arr))
