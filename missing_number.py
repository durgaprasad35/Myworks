def missingFind(arr): 
    n = len(arr)+1 
    sum = n * (n+1)//2 
    for i in arr:
        sum = sum - i 
    return sum 
arr = [1,3,5,2,4,7,9,10,6] 
result = missingFind(arr) 
print(result) 