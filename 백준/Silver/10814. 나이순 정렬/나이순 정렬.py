n = int(input())

people = [tuple(input().split()) for _ in range(n)]

people_sorted = sorted(people, key=lambda x: int(x[0]))

for person in people_sorted:
    print(person[0], person[1])
