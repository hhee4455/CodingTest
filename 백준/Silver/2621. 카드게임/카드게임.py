from collections import Counter

color_array = []
num_array = []

for i in range(5):
    col, num = input().split()
    color_array.append(col)
    num_array.append(int(num)) 

num_array.sort()

count = Counter(num_array)

# 색이 모두 같을 때
if len(set(color_array)) == 1:
    # 숫자가 연속적일 때 (1번)
    if all(num_array[i] - num_array[i - 1] == 1 for i in range(1, 5)):
        print(900 + max(num_array))
    # 숫자가 연속적이지 않을 때 (4번)
    else:
        print(600 + max(num_array))
else:
    # 숫자가 연속적일 때 (5번)
    if all(num_array[i] - num_array[i - 1] == 1 for i in range(1, 5)):
        print(500 + max(num_array))
    else:
        # 5개 중에 4개가 같을 때 (2번)
        if 4 in count.values():
            four_of_a_kind = [key for key, value in count.items() if value == 4]
            print(800 + four_of_a_kind[0])
        # 5개 중에 3개 2개가 같을 때 (3번)
        elif 3 in count.values() and 2 in count.values():
            three_of_a_kind = [key for key, value in count.items() if value == 3]
            two_of_a_kind = [key for key, value in count.items() if value == 2]
            print(700 + (three_of_a_kind[0] * 10) + two_of_a_kind[0])
        # 5개 중에 3개가 같을 때 (6번)
        elif 3 in count.values():
            three_of_a_kind = [key for key, value in count.items() if value == 3]
            print(400 + three_of_a_kind[0])
        # 5개 중에 2개 2개가 같을 때 (7번)
        elif list(count.values()).count(2) == 2:
            pairs = sorted([key for key, value in count.items() if value == 2], reverse=True)
            print(300 + (pairs[0] * 10) + pairs[1])
        # 5개 중에 2개가 같을 때 (8번)
        elif 2 in count.values():
            two_of_a_kind = [key for key, value in count.items() if value == 2]
            print(200 + two_of_a_kind[0])
        # 어떤 경우에도 해당하지 않을 때
        else:
            print(100 + max(num_array))
