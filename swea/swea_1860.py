T = int(input())

for test_case in range(1, T + 1):

    # 1860. 진기의 최고급 붕어빵
    N, M, K = map(int, input().split())
    visit = [int(x) for x in input().split()]

    possible = True
    prev_v = 0
    making_time = 0
    boong = 0

    for v in sorted(visit):
        # 다음 손님이 오기까지 걸린 시간
        making_time += v - prev_v
        
        # 진기가 그 동안 만든 붕어빵의 양
        boong += (making_time // M) * K

        # 시간 소모
        making_time -= (making_time // M) * M

        prev_v = v

        if boong > 0:
            boong -= 1
        else:
            possible = False
            break

    if possible:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')
