def maxMin(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        if arr[low] > arr[high]:
            return arr[low],arr[high]
        else:
            return arr[high],arr[low]
    mid = (low + high) // 2
    max1, min1 = maxMin(arr, low, mid)
    max2, min2 = maxMin(arr, mid + 1, high)
    max_final = max(max1, max2)
    min_final = min(min1, min2)
    return max_final, min_final
arr = [1, 4, 5, 6, 76, 90, 10,400,500,2000]
low = 0
high = len(arr) - 1 
result = maxMin(arr, low, high)
print("Max:", result[0])
print("Min:", result[1])    
