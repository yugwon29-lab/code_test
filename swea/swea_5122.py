T = int(input())

for test_case in range(1, T + 1):

    # 5122. 수열 편집
    N, M, L = map(int, input().split())
    numbers = [int(x) for x in input().split()]

    for i in range(M):
        cmd = [x for x in input().split()]
        if cmd[0] == 'I':
            numbers.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            numbers.pop(int(cmd[1]))
        elif cmd[0] == 'C':
            numbers[int(cmd[1])] = int(cmd[2])

    if not (0 <= L < len(numbers)):
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {numbers[L]}')