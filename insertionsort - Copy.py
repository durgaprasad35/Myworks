def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i] 
        j = i-1 
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j-=1 
        arr[j+1] = key 
arr = [100,20,500,50,12] 
insertionsort(arr) 
print(f"The sorted array is {arr}")   