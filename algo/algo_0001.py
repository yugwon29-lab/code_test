# 연습 문제 2
# Gravity

# 입력 받기
N = int(input())
boxes = list(map(int, input().split()))

# 낙차 구하기
max_height = 0

for i in range(N):
    cnt_box = 0
    for j in range(i + 1, N):
        if boxes[i] <= boxes[j]:
            cnt_box += 1
    height = N - 1 - i - cnt_box
    if max_height < height:
        max_height = height

print(f"{max_height}")
