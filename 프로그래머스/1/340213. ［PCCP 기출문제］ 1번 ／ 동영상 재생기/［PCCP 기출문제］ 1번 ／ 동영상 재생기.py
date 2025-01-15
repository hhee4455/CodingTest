def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 분 단위로 변환하는 함수
    def time_to_minutes(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    video = time_to_minutes(video_len)
    pos = time_to_minutes(pos)
    op_s = time_to_minutes(op_start)
    op_e = time_to_minutes(op_end)
    
    if op_s <= pos <= op_e:
        pos = op_e

    for func in commands:
        if func == "next":
            pos += 10 
        elif func == "prev":
            pos -= 10 

        if pos < 0:
            pos = 0
        elif pos > video:
            pos = video

        if op_s <= pos <= op_e:
            pos = op_e

    final_h = pos // 60
    final_m = pos % 60
    return f"{str(final_h).zfill(2)}:{str(final_m).zfill(2)}"
