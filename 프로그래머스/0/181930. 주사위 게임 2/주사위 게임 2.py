def solution(a, b, c):
    array = [a,b,c]
    set_array = set(array)
    if len(set_array) == 3:
        return a+b+c
    elif len(set_array) == 2:
        return (a+b+c) * (a ** 2 + b ** 2 + c **2)
    elif len(set_array) == 1:
        return (a+b+c) * (a ** 2 + b ** 2 + c **2) * (a ** 3 + b ** 3 + c **3)
        