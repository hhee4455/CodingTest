def solution(numbers, target):
    answer = 0
    
    def dfs(i,current_sum):
        nonlocal answer
        
        if i == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        dfs(i+1,current_sum + numbers[i])
        dfs(i+1,current_sum - numbers[i])
    
    dfs(0,0)
    return answer