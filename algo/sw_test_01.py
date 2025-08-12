# 삼성전자는 수원삼성 구단의 홍보를 위해 축구장에 4행 n열 크기의 LED 디스플레이를 설치하였다.
# LED 디스플레이의 각 픽셀은 1(ON)과 0(OFF)의 2가지 상태를 가지며 일정한 주기로 다음과 같이 변한다.

# 픽셀 (i, j)는 i열 j행에 위한 픽셀을 의미하며,
# 픽셀 (i, j)는 (i+j+1)이 시간 k의 배수이면, 현 상태에서 다른 상태로 바뀐다.
# 즉, 0(OFF)는 1(ON)으로, 1(ON)은 0(OFF)로 바뀐다.

# 시간이 0일 때 각 픽셀은 0(OFF)으로 초기화되어 있다.

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    R, C = 4, N

    def div(n, K):
        cnt = 0
        for k in range(1, K+1):
            if n % k == 0:
                cnt += 1
        if cnt % 2 == 0:
            return False
        else:
            return True
    
    cnt_on = 0
    for r in range(R):
        for c in range(C):
            if div(r+c+1, K):
                cnt_on += 1
    
    print(f'#{t} {cnt_on}')
