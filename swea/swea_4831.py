T = int(input())

for i in range(1, T + 1):

    # 4831.전기버스
    K, N, M = map(int, input().split())
    a = [int(x) for x in input().split()]

    # 배터리 충전
    battery = K
    # 버스 시작 지점
    bus = 0
    # 충전 횟수
    charge = 0

    while bus != N:
        # 버스 최대 운전 거리
        max_bus = bus + K
        bus_range = range(bus + 1, max_bus + 1)
        if N in bus_range:
            # 버스 도착
            break
        charge_point = None
        for b in bus_range:
            if b in a:
                charge_point = b
        if charge_point is None:
            # 버스 도달 불가
            charge = 0
            break
        else:
            # 버스 충전
            charge += 1
            bus = charge_point

    print(f'#{i} {charge}')