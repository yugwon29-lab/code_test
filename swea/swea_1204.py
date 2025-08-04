T = int(input())

for test_case in range(1, T + 1):

    # 1204. 최빈수 구하기
    N = int(input())
    array = [int(x) for x in input().split()]

    num_array = [0] * 101

    for score in array:
        num_array[score] += 1

    freq_score = 0

    for score in range(1, 101):
        if num_array[freq_score] <= num_array[score]:
            freq_score = score

    print(f"#{N} {freq_score}")
