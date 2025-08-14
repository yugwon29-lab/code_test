# 10773. 제로
from collections import deque

stack = deque()

K = int(input())
total = 0

for _ in range(K):
    num = int(input())
    if num == 0:
        total -= stack.pop()
    else:
        total += num
        stack.append(num)

print(total)