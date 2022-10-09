def selection(arr):
    for i in range(len(arr)):
        min_ = i
        for j in range(i+1, len(arr)):
            if arr[min_] > arr[j]:
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr

arr = [40, 23, 7, 49, 32, 98, 76, 48, 87]
print(selection(arr))
