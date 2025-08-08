# 글자수

T = int(input())

for t in range(1, T+1):

    str1 = list(input())
    str2 = list(input())

    max_cnt = 0

    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{t} {max_cnt}')