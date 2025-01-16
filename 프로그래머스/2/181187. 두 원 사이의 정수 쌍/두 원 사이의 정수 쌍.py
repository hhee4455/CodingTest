import math

def solution(r1, r2):
    answer = 0
    degree = 1
    x_bias = [1, r2]

    for i in range(1, r2):
        if r1 > i:
            min_y = math.pow(r1, 2) - math.pow(i, 2)
            max_y = math.pow(r2, 2) - math.pow(i, 2)

            if 0<= min_y and 0<= max_y:
                min_y = math.sqrt(min_y)
                max_y = math.sqrt(max_y)

                min_y = math.ceil(min_y) 
                max_y = math.floor(max_y)

                answer += max_y - min_y + 1
        else:
            max_y = math.floor(math.sqrt(math.pow(r2, 2) - math.pow(i, 2)))
            answer += max_y + 1

    answer += 1
    answer = answer * 4

    return answer
