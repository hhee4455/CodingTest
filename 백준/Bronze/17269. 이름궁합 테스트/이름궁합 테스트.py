alphabet_strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n, m = map(int, input().split())
A, B = input().split()

combined = []
min_len = min(n, m)
for i in range(min_len):
    combined.append(A[i])
    combined.append(B[i])

if n > m:
    combined.extend(A[m:])
elif m > n:
    combined.extend(B[n:])

numbers = [alphabet_strokes[ord(char) - ord('A')] for char in combined]

while len(numbers) > 2:
    numbers = [(numbers[i] + numbers[i + 1]) % 10 for i in range(len(numbers) - 1)]

result = numbers[0] * 10 + numbers[1]
print(f"{result}%" if result >= 10 else f"{numbers[1]}%")
