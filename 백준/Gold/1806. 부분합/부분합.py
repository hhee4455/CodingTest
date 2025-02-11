import sys

def min_length_subarray(n, s, arr):
    start, end = 0, 0
    min_length = float('inf')  
    total = 0

    while end < n:
        total += arr[end]  

        while total >= s:  
            min_length = min(min_length, end - start + 1)
            total -= arr[start]  
            start += 1 

        end += 1  

    return min_length if min_length != float('inf') else 0  


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(min_length_subarray(n, s, arr))
