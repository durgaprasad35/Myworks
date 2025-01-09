def linearsearch(arr,target):
    for i in range(len(arr)): 
        if arr[i]==target:
            return i 
    return -1 
arr = [1,2,3,4,5,6,80] 
target = 80 
result = linearsearch(arr,target) 
if result!=-1:
    print(f"The target is {result} is found") 
else:
    print(f"The target {target} is not found!!") 

        