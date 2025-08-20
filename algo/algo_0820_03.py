# 암호생성기

T = 10

for _ in range(T):
    t = int(input())
    num = [int(x) for x in input().split()]

    # now : 현재 숫자
    now = 0
    down = 1

    while True:
        # 감소시키고 뒤로 이동한다.
        num[now] -= down
        # 0보다 작아지거나 0일 경우 종료.
        if num[now] <= 0:
            num[now] = 0
            now = (now + 1) % 8
            break
        now = (now + 1) % 8
        down += 1
        if down > 5:
            down = down % 5

    print(f'#{t}', end=' ')
    for i in range(8):
        print(f'{num[now]}', end=' ')
        now = (now + 1) % 8
    print()
