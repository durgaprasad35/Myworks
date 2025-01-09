def quickSort(arr):
    if len(arr)<=1:
        return arr 
    pivot = arr[len(arr)//2] 
    left = [i for i in arr if i<pivot] 
    middle = [i for i in arr if i==pivot] 
    right = [i for i in arr if i>pivot]
    return quickSort(left)+middle+quickSort(right) 
arr = [10, 7, 8, 9, 1, 5]
sorted_arr_as = quickSort(arr)
print("Sorted array in ascending order:", sorted_arr_as)
 


