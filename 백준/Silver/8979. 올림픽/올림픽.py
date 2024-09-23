n, k = map(int, input().split())
medal_data = []

for _ in range(n):
    country_data = list(map(int, input().split()))
    medal_data.append(country_data)

sorted_medal_data = sorted(medal_data, key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
previous_values = (-1, -1, -1) 
k_rank = 0 


for i, data in enumerate(sorted_medal_data):
    current_values = (data[1], data[2], data[3]) 
    
    if current_values != previous_values:
        rank = i + 1  
    
    if data[0] == k:
        k_rank = rank
        break
    
    previous_values = current_values

print(k_rank)
