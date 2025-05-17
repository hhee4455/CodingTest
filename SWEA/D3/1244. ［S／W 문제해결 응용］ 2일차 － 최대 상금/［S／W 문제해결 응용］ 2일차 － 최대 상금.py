T = int(input())

for test_case in range(1, T + 1):
    raw, cnt = input().split()
    cnt = int(cnt)
    nums = list(raw)

    visited = set()
    answer = [0]

    def dfs(current, depth):
        key = (''.join(current), depth)
        if key in visited:
            return
        visited.add(key)

        if depth == cnt:
            answer[0] = max(answer[0], int(''.join(current)))
            return
        
        for i in range(len(current)):
            for j in range(i+1, len(current)):
                current[i], current[j] = current[j], current[i]
                dfs(current, depth + 1)
                current[i], current[j] = current[j], current[i]
    
    dfs(nums, 0)
    print(f"#{test_case} {answer[0]}")
