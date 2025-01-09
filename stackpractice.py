def stack(arr):
    maxi = max(arr)
    n = len(arr)

    for i in range(n):
        if arr[i] <= maxi:
            print(maxi)
        else:
            return -1  # Immediately return -1 if any element is greater than maxi

    return 0  # Return 0 if all elements are processed without issue
    
arr = [6, 5, 3, 6]
result = stack(arr)
print(result)
