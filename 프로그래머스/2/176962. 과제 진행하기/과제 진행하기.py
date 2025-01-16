def solution(plans):
    array = []

    def time_change(time, do):
        hh, mm = map(int, time.split(':'))
        do_int = int(do)
        time_int = (hh * 60) + mm
        return time_int, do_int

    for plan in plans:
        start, playtime = time_change(plan[1], plan[2])
        array.append((plan[0], start, playtime))

    array.sort(key=lambda x: x[1])  # 시작 시간을 기준으로 정렬
    result = []
    paused = []  # 멈춘 과제를 관리하는 스택

    current_time = 0
    for i in range(len(array)):
        name, start, duration = array[i]

        # 진행 중인 과제를 끝내고 새 과제를 시작해야 한다면
        while paused and current_time < start:
            paused_name, remaining_time = paused.pop()
            if current_time + remaining_time <= start:
                result.append(paused_name)  # 과제를 완료
                current_time += remaining_time
            else:
                paused.append((paused_name, remaining_time - (start - current_time)))
                break

        # 새 과제 시작
        current_time = max(current_time, start)
        if i < len(array) - 1 and current_time + duration > array[i + 1][1]:
            paused.append((name, duration - (array[i + 1][1] - current_time)))
            current_time = array[i + 1][1]
        else:
            result.append(name)
            current_time += duration

    # 남아 있는 멈춘 과제 처리
    while paused:
        paused_name, remaining_time = paused.pop()
        result.append(paused_name)

    return result
