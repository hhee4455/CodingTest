def solution(s):
    result = []
    
    for index, char in enumerate(s):
        if char in s[:index]:
            last_occurrence = s[:index].rfind(char) 
            result.append(index - last_occurrence) 
        else:
            result.append(-1) 
    
    return result
