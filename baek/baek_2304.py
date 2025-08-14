# 2304. 창고 다각형

N = int(input())
col = [0] * (1000+1)

min_w, max_w = 10000, -1
max_height = 0
for _ in range(N):
    l, h = map(int, input().split())
    if h > max_height:
        max_height = h
    if min_w > l:
        min_w = l
    if max_w < l:
        max_w = l
    col[l] = h

area = 0
now_max_up = 0
first_max = -1
second_max = -1
for i in range(min_w, max_w+1):
    if max_height == col[i]:
        first_max = i
        break
    if now_max_up < col[i]:
        now_max_up = col[i]
    area += now_max_up

now_max_up = 0
for j in range(max_w, min_w-1, -1):
    if max_height == col[j]:
        second_max = j
        break
    if now_max_up < col[j]:
        now_max_up = col[j]
    area += now_max_up

for k in range(first_max, second_max+1):
    area += max_height

print(area)