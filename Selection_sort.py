def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
	    smallest = arr[i]
	    smallest_index=i
    return smallest_index
	
def selection_sort(arr):
    sortArr = []
    for i in range(len(arr)):
	smallest = find_smallest(arr)
        sortArr.append(arr.pop(smallest))
    return sortArr

arr = input().split()
n = 0
for i in arr:
    arr[n] = int(i)
    n+=1
print(selection_sort(arr))
