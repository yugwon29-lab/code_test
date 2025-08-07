# 이진탐색

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())

    l_a, l_b = 1, 1
    r_a, r_b = P, P
    find_a, find_b = 0, 0

    while not (find_a or find_b):
        # A 먼저 탐색
        c_a = (l_a + r_a) // 2
        if c_a == A:
            find_a = 1
        elif c_a < A:
            l_a = c_a
        else:
            r_a = c_a
        
        # B 탐색
        c_b = (l_b + r_b) // 2
        if c_b == B:
            find_b = 1
        elif c_b < B:
            l_b = c_b
        else:
            r_b = c_b

    if find_a and not find_b:
        print(f'#{t} A')
    elif not find_a and find_b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')