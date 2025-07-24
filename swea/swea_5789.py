T = int(input())

for test_case in range(1, T + 1):

    # 5789. 현주의 상자 바꾸기
    N, Q = map(int, input().split())

    boxes = [0] * (N+1)

    for q in range(Q):
        L, R = map(int, input().split())
        boxes[L:R+1] = [q+1] * (R-L+1)

    for i in range(len(boxes)):
        if i == 0:
            print(f'#{test_case}', end=' ')
        elif i == len(boxes) - 1:
            print(boxes[i])
        else:
            print(boxes[i], end=' ')