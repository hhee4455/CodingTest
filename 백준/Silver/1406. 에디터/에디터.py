import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

def solution(left_stack, right_stack, cuser):
    if cuser[0] == "P":
        left_stack.append(cuser[1]) 

    elif cuser[0] == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop())  
            
    elif cuser[0] == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())  
            
    elif cuser[0] == "B":
        if left_stack:
            left_stack.pop()  

word = list(input().strip()) 
n = int(input().strip())
cusers = [input().strip().split() for _ in range(n)]

left_stack = deque(word)
right_stack = deque() 

for cuser in cusers:
    solution(left_stack, right_stack, cuser)

print("".join(left_stack) + "".join(right_stack))