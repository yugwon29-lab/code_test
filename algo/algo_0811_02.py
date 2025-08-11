# 가장 빠른 문자열 타이핑

T = int(input())

for t in range(1, T+1):
    A, B = input().split()

    # A의 길이, B의 길이
    len_a, len_b = len(A), len(B)

    type_cnt = 0

    # 타이핑 시작
    i = 0
    while i < len_a:
        # 만약 문자가 B의 앞 글자와 다르다면, 그냥 그 글자를 누른다.
        if A[i] != B[0]:
            type_cnt += 1
        # 같다면, B로 칠 수 있는지 확인한다.
        else:
            if i + len_b - 1 < len_a:
                check_a, check_b = i, 0
                can_type = True
                for j in range(1, len_b):
                    if A[i+j] != B[j]:
                        can_type = False
                        break
                if can_type:
                    type_cnt += 1
                    i += len_b
                    continue
            type_cnt += 1
        i += 1
    
    print(f'#{t} {type_cnt}')