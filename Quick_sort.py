def quick_sort(arr):
    if len(arr) < 2:
	return arr
    else:
	pivot = arr[0]
	less = [i for i in arr[1:] if i <= pivot]
	greater = [i for i in arr[1:] if i > pivot]
	return quick_sort(less) + [pivot] + quick_sort(greater)

arr = input().split()
n = 0

for i in arr:
    arr[n] = int(i)
    n +=1

qs = quick_sort(arr)
print(qs)
