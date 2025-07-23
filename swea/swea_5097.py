T = int(input())

for test_case in range(1, T + 1):

    # 5097. 회전
    N, M = map(int, input().split())
    num = [int(x) for x in input().split()]

    # 큐 선언
    queue = []

    # 맨 앞의 숫자 뒤로 보내기
    for i in range(M):
        queue.append(num.pop(0))
        num.append(queue.pop(0))

    print(f'#{test_case} {num[0]}')