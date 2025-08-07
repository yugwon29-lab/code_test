# 연습 문제 3
# 대각선 원소의 합

T = int(input())

for test_case in range(1, T + 1):
    # 입력 받기
    N = int(input())
    boxes = [[int(x) for x in input().split()] for _ in range(N)]

    c = N // 2
    sum_value = 0
    
    # 중심 더하기
    sum_value += boxes[c][c]

    # 나머지 대각선 성분 더하기
    for m in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        for k in range(1, c+1):
            sum_value += boxes[c+m[0]*k][c+m[1]*k]

    print(f'#{test_case} {sum_value}')