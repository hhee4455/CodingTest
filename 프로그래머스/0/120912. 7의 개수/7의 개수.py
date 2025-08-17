def solution(array):
    answer = 0
    
    for arr in array:
        arr_str = str(arr)
        for a_str in arr_str:
            if a_str == "7":
                answer += 1
        
    return answer