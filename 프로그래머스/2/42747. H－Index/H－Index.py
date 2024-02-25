def solution(citations):
    citations.sort(reverse=True)  
    n = len(citations)
    h_index = 0
    
    for i, citation in enumerate(citations):
        if citation >= i + 1:  
            h_index = i + 1    
    
    return h_index