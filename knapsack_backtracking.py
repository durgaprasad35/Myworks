def knapsack_backtracking(values,weights,capacity):
    def backtrack(index,remaining_capacity,current_value):
        if index==len(values) or remaining_capacity == 0:
            return current_value 
        max_value = backtrack(index+1,remaining_capacity,current_value) 
        if weights[index] <= remaining_capacity:
            max_value = max(max_value,backtrack(index+1,remaining_capacity-weights[index],current_value+values[index])) 
        return max_value 
    return backtrack(0,capacity,0) 
values = [60,100,120] 
weights = [10,20,30] 
capacity = 50
max_value = knapsack_backtracking(values,weights,capacity)  
print(f"The maximum profit is {max_value}") 
