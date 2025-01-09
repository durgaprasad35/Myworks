import heapq 
def optimal_merge_pattern(file_sizes):
    if not file_sizes:
        return 0 
    heapq.heapify(file_sizes) 
    total_cost = 0 
    while len(file_sizes)>1:
        first = heapq.heappop(file_sizes) 
        second = heapq.heappop(file_sizes) 
        merged_file = first + second 
        total_cost += merged_file 
        heapq.heappush(file_sizes,merged_file) 
    return total_cost 
file_sizes = [10,20,30,40] 
min_cost = optimal_merge_pattern(file_sizes) 
print(f"The minimum cost is {min_cost}")