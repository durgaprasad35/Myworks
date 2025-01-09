def binarysearch(arr,target):
    left = 0 
    right = len(arr)-1 
    while left<=right:
        mid = (left+right)//2 
        if arr[mid]==target:
            return mid 
        elif arr[mid]<target:
            left = mid+1 
        else:
            right = mid-1 
    return -1 
arr = [2,1,3,45,78,5,7,85,321,40] 
print(f"The given  array is {arr}") 
arr.sort() 
print(f"The sorted array is {arr}")
target = 40 
result = binarysearch(arr,target) 
if result!=-1:
    print(f"The {target} is found in the array at index {result}") 
else:
    print(f"The {target} is not found in the array") 