import random

lines = []

T = 5
lines.append(f"{T}")
for _ in range(T):
    N = random.randint(5, 1000)
    min = int(N / 4)
    max = int(N / 2)
    lines.append(f"{N} {min} {max}")
    scores = []
    for i in range(N):
        scores.append(random.randint(1, 100))
    scores = [str(s) for s in scores]
    lines.append(f"{' '.join(scores)}")

with open('testcase.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
