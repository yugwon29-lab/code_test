# 1일차 min max

T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N = int(input())
    arr_a = list(map(int, input().split()))

    # 첫 번째 값이 가장 큰 값, 가장 작은 값이라 가정한다.
    max_v, min_v = arr_a[0], arr_a[0]

    for i in range(1, N):
        # 최대값 찾기
        if max_v < arr_a[i]:
            max_v = arr_a[i]
        # 최소값 찾기
        if min_v > arr_a[i]:
            min_v = arr_a[i]

    result = max_v - min_v
    print(f"#{test_case} {result}")
