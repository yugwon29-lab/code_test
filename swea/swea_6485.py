T = int(input())

for test_case in range(1, T + 1):

    # 6485. 삼성시의 버스 노선
    N = int(input())
    buses = []
    for b in range(N):
        A, B = map(int, input().split())
        buses.append((A, B))

    P = int(input())

    result = []
    for p in range(P):
        C = int(input())
        num_bus = 0
        for bus in buses:
            if bus[0] <= C <= bus[1]:
                num_bus += 1
        result.append(num_bus)

    print(f'#{test_case}', end=' ')
    for r in result:
        print(r, end=' ')
    print()