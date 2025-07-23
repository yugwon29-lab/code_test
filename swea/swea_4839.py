T = int(input())

for i in range(1, T + 1):

    # 4839. 이진탐색
    P, A, B = map(int, input().split())

    num_A = 0
    num_B = 0

    l_a, r_a, c_a = 1, P, 0
    l_b, r_b, c_b = 1, P, 0

    while A != c_a:
        # A 탐색
        num_A += 1

        c_a = int((l_a + r_a) / 2)
        if A < c_a:
            r_a = c_a
        else:
            l_a = c_a

    while B != c_b:
        # B 탐색
        num_B += 1

        c_b = int((l_b + r_b) / 2)
        if B < c_b:
            r_b = c_b
        else:
            l_b = c_b

    if num_A < num_B:
        print(f"#{i} A")
    elif num_A > num_B:
        print(f"#{i} B")
    else:
        print(f"#{i} 0")