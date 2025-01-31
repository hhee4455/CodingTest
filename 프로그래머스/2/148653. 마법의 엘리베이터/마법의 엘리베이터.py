def solution(storey):
    result = 0
    
    while storey > 0:
        digit = storey % 10
        
        if digit > 5: 
            result += (10 - digit)
            storey += 10
        elif digit < 5: 
            result += digit
        else:  
            if (storey // 10) % 10 >= 5: 
                result += 5
                storey += 10
            else: 
                result += 5
        
        storey //= 10 
    
    return result
