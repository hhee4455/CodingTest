def solution(k, d):
    result = 0
    d_squared = d * d
    
    for x in range(0,d+1,k):
        max_y = int((d_squared - x * x) ** 0.5)
        result += (max_y // k) + 1
        
    return result