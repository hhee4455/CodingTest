from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (우선순위, 인덱스)
    count = 0
    
    while queue:
        max_priority = max(queue, key=lambda x: x[0])[0]  # 현재 큐에서 최대 우선순위 찾기
        priority, idx = queue.popleft()  # 첫 번째 문서 꺼내기
        
        if priority < max_priority:  # 현재 문서보다 높은 우선순위가 존재하면 다시 큐에 넣기
            queue.append((priority, idx))
        else:  # 출력 가능
            count += 1
            if idx == location:  # 원하는 문서라면 출력 순서 반환
                return count
