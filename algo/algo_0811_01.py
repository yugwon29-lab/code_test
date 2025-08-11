# 문자열 비교

T = int(input())

for t in range(1, T+1):
    # 입력받기
    str1 = input()
    str2 = input()

    M = len(str1)
    N = len(str2)

    i = 0   # str2의 인덱스
    j = 0   # str1의 인덱스

    while j < M and i < N:
        if str2[i] != str1[j]:
            i -= j
            j = -1
        i += 1
        j += 1

    if j == M:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')