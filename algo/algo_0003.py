# 연습 문제 4
# 이웃한 요소에 대한 차의 절대값의 합을 구하세요.

T = int(input())

for test_case in range(1, T + 1):
    # 입력 받기
    N = int(input())
    boxes = [[int(x) for x in input().split()] for _ in range(N)]

    sum_value = 0
    for i in range(N):
        for j in range(N):
            for m in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= i+m[0] < N) and (0 <= j+m[1] < N):
                    sum_value += abs(boxes[i+m[0]][j+m[1]] - boxes[i][j])

    print(f'#{test_case} {sum_value}')