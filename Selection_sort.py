from random import randint


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


arr =[]
for _ in range(20):
    arr.append(randint(-30, 30))

print(arr)
print(selection_sort(arr))

