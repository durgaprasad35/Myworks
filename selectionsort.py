def selectionSort(arr):
    for i in range(len(arr)):
        low =i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[low]:
                low = j 
        arr[i],arr[low] = arr[low],arr[i] 
arr = list(map(int,input().split())) 
selectionSort(arr) 
print(f"The aorted array is {arr}")
        