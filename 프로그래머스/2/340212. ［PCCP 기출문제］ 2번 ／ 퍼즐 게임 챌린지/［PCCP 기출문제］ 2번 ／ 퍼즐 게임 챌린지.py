def solution(diffs, times, limit):
    def calculate_time(level):
        time_used = 0
        prev_time = 0
        
        for i in range(len(diffs)):
            if level >= diffs[i]:
                time_used += times[i]
            else:
                num_errors = diffs[i] - level
                time_used += num_errors * (times[i] + prev_time) + times[i]
            
            prev_time = times[i]
        
        return time_used

    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        time_needed = calculate_time(mid)

        if time_needed <= limit:
            answer = mid 
            right = mid - 1
        else:
            left = mid + 1

    return answer
