def solution(myStr):
    answer = []
    char  = ['a', 'b', 'c']
    Str = list(myStr)
    word = []
    
    for i in range(len(Str)):
        if Str[i] not in char:
            word.append(Str[i])
        else:
            if word:
                answer.append(''.join(word))
            word = []

    if word:
        answer.append(''.join(word))
    
    return answer if answer else ["EMPTY"]