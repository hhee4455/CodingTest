from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine) 
    sorted_counts = sorted(count.values(), reverse=True) 
    
    total = 0  
    kind_count = 0  
    
    for c in sorted_counts:
        total += c  
        kind_count += 1  
        
        if total >= k:  
            return kind_count
    
    return kind_count  

