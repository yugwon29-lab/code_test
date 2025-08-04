# 1일차 구간합

T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))

    # 최대값, 최소값 입력
    max_sum, min_sum = None, None

    # 구간합 계산 및 최대값, 최소값 설정
    # 구간은 총 N-M+1개가 존재
    for i in range(N - M + 1):
        # 구간 범위
        add_range = range(i, i + M)
        # 구간 합 계산
        sum_value = 0
        for j in add_range:
            sum_value += arr_a[j]
        # 최대값, 최소값 갱신
        if max_sum is None and min_sum is None:
            max_sum = sum_value
            min_sum = sum_value
        else:
            if max_sum < sum_value:
                max_sum = sum_value
            if min_sum > sum_value:
                min_sum = sum_value

    # 최대값과 최소값의 차이 계산
    result = max_sum - min_sum
    print(f"#{test_case} {result}")
