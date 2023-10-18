def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

# Test the implementation with an example list.

arr = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", arr)
print("The sorted list is: ", bubble_sort(arr))
