# 1일차 View

T = 10

for test_case in range(1, T + 1):

    # 입력 받기
    N = int(input())
    arr_a = list(map(int, input().split()))

    # 조망권 확보
    view = [-2, -1, +1, +2]

    # idx번째 건물에서 조망권이 확보된 세대를 구하는 함수
    def check_view(idx):
        # 조망권이 확보된 세대가 없는 경우가 최악.
        min_diff = None
        for v in view:
            # 범위 내 높이가 높거나 같은 건물이 하나라도 있으면 해당 건물엔 조망권 확보 세대 없음.
            if arr_a[idx] <= arr_a[idx + v]:
                min_diff = 0
                break
            # 그 외의 경우만 있다면, 높이차가 가장 작은 수가 조망권이 확보된 세대 수
            else:
                diff = arr_a[idx] - arr_a[idx + v]
                if min_diff is None:
                    min_diff = diff
                else:
                    if diff < min_diff:
                        min_diff = diff

        return min_diff

    total_view = 0
    for i in range(2, N - 2):
        total_view += check_view(i)

    print(f"#{test_case} {total_view}")
