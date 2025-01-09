def fractional_knapsack(weights,values,capacity):
    n= len(weights) 
    items = [(weights[i]/values[i],values[i],weights[i]) for i in range(n)] 
    items.sort(reverse=True,key=lambda x:x[0]) 
    total_value = 0 
    remaining_capacity = capacity 
    for ratio,value,weight in items: 
        if remaining_capacity == 0:
            break 
        if weight <=remaining_capacity:
            total_value+=value 
            remaining_capacity-=weight 
        else:
            total_value+=ratio*remaining_capacity 
            remaining_capacity = 0 
    return total_value 
weights = [20,30,40,50] 
values = [20,6 ,27,5] 
capacity = 50 
max_profit = fractional_knapsack(weights,values,capacity) 
print(f"The maximum profit is {max_profit}") 