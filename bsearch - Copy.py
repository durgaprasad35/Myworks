def binarySearch(arr,target):
    low = 0 
    high = len(arr)-1
    for i in range(len(arr)):
        mid = low+high//2 
        if arr[mid] == target:
            return mid 
        elif arr[mid]<target:
            low = mid+1 
        else:
            high = mid -1 
    return -1 
arr = [1,2,3,4,5,6,8,8,77645,56] 
target = 56 
res = binarySearch(arr,target) 
if res!=-1:
    print(f"The target is found at index {res}") 
else:
    print("The target is not found!!")