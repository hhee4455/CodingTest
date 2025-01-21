def solution(keymap, targets):
    min_index_map = {}
    
    for key in keymap:
        for idx, char in enumerate(key):
            if char in min_index_map:
                min_index_map[char] = min(min_index_map[char], idx)
            else:
                min_index_map[char] = idx

    result = []
    
    for target in targets:
        count = 0
        for char in target:
            if char in min_index_map:
                count += min_index_map[char] + 1
            else:
                count = -1
                break
        result.append(count)
    
    return result
