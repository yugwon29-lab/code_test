T = int(input())

for test_case in range(1, T + 1):

    # 5108. 숫자 추가
    N, M, L = map(int, input().split())
    num_row = [int(x) for x in input().split()]
    for i in range(M):
        idx, n = map(int, input().split())
        num_row.insert(idx, n)

    print(f'#{test_case} {num_row[L]}')


