def solution(s):
    s_arr = list(s)
    if len(s_arr) % 2 == 0:
        return s_arr[len(s_arr)//2 - 1] + s_arr[len(s_arr)//2]
    else:
        return s_arr[len(s_arr)//2]
