from collections import Counter

n = int(input())
word = input()
words = [input() for _ in range(n-1)]
count = 0

word_count = Counter(word)

for w in words:
    w_count = Counter(w)

    if word_count == w_count:
        count += 1
        continue

    elif len(word) == len(w):
        diff = sum((word_count - w_count).values()) + sum((w_count - word_count).values())
        if diff == 2:
            count += 1
        continue
        
    elif abs(len(word) - len(w)) == 1:
        big, small = (word_count, w_count) if len(word) > len(w) else (w_count, word_count)
        diff = sum((big - small).values())
        if diff == 1:
            count += 1
        continue

print(count)
