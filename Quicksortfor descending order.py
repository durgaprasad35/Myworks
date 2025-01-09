def quickSort(arr):
    if len(arr)<=1:
        return arr 
    else:
        key = arr[len(arr)//2] 
        small = [x for x in arr if x<key] 
        middle = [x for x in arr if x==key] 
        large = [x for x in arr if x>key] 
        return quickSort(large)+middle+quickSort(small) 
arr = [10,23,5,545,23,134,35,5] 
sorted_arr_ds = quickSort(arr) 
print("The sorted array is:-",sorted_arr_ds)
