def optimal_merge_pattern(file_sizes):
    if not file_sizes:
        return 0 
    file_sizes.sort() 
    total_cost = 0 
    while len(file_sizes)>1:
        fisrt = file_sizes.pop(0) 
        second = file_sizes.pop(0) 
        merged_file = fisrt+second 
        total_cost+=merged_file 
        index = 0 
        while index < len(file_sizes) and file_sizes[index]<merged_file:
            index+=1 
        file_sizes.insert(index,merged_file) 
    return total_cost 
file_sizes = [10,20,30] 
min_cost = optimal_merge_pattern(file_sizes) 
print(f"The minimum cost is {min_cost}") 