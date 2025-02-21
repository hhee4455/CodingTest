from collections import Counter

def solution(s):
    s_count = Counter(s)  # 문자 개수 세기
    
    if len(set(s)) == 1:
        return False
    
    if s_count.get('(') != s_count.get(')'):
        return False
    
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

