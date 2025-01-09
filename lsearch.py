def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1 
arr = [1,2,3,45,78,90] 
target = 90 
res=linearSearch(arr,target) 
if res!=-1:
    print(f"The target{target} is found at index {res}") 
else:
    print("The target is not found!!")