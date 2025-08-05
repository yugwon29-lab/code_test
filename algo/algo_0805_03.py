# 전기 버스

T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    K, N, M = map(int, input().split())
    charge = [int(x) for x in input().split()]

    # 배터리
    bus = 0
    num_charge = 0
    
    while True:
        bus_range = range(bus + 1, bus + K + 1)
        can_go = False
        # 버스가 가는 길에 갈 수 있는 가장 먼 충전소 찾기
        for b in bus_range:
            if b in charge:
                can_go = True
                b_idx = b
            # 버스가 도착할 수 있다면,
            if b == N:
                can_go = False
                break

        # 갈 수 없거나 버스가 도착지를 지나칠 수 있다면, 버스는 최대한 가고 멈춘다.
        if not can_go:
            bus = bus + K
            break
        else:
            # 갈 수 있다면, 버스는 그 충전소까지 가고 충전한다.
            bus = b_idx
            num_charge += 1

    if bus < N:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {num_charge}')

