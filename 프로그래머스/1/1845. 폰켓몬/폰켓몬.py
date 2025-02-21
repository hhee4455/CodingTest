def solution(nums):
    get = len(nums)//2
    
    return len(set(nums)) if get >= len(set(nums)) else get