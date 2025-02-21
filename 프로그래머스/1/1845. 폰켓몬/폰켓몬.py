def solution(nums):
    get = len(nums)//2
    nums_set = set(nums)
    
    return len(list(nums_set)) if get >= len(nums_set) else get