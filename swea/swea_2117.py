from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    # 2117. 홈 방범 서비스
    
    # 입력 받기
    N, M = map(int, input().split())
    home_map = [[int(x) for x in input().split()] for _ in range(N)]
    