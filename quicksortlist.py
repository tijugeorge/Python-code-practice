def quicksort(array):
  if len(array) <= 1:
    return array
  pivot = array[len(array)/2]
  left = [x for x in array if x < pivot]
  middle = [x for x in array if x == pivot]
  right = [x for x in array if x > pivot]
  return quicksort(left) + middle + quicksort(right)


array = [2,9,4,8,2,6,4,0,2,7,4,5,9,2,8,4,0]

print quicksort(array)
