def solution(t, p):
    num_arr = []
    t = list(t)
    p_len = len(list(p))
    index = 0
    count = 0
    
    while index < len(t):
        num = t[index:index + p_len]
        
        if len(num) < p_len:
            break
        
        if int(''.join(num)) <= int(p):
            count += 1
        
        index += 1
    return count
        
        
        
        
        