# 증가하는 사탕 수열
T = int(input())

for t in range(1, T+1):
    A, B, C = map(int, input().split())

    # 절대 불가능
    if B < 2 or C < 3:
        print(f'#{t} -1')
        continue

    # 먹은 사탕의 수
    candy = 0

    # B를 C에 대해 우선 맞춘다.
    if B >= C:
        eat_b = B - C + 1
        B -= eat_b
        candy += eat_b
    
    # A를 B에 대해 맞춘다.
    if A >= B:
        eat_a = A - B + 1
        A -= eat_a
        candy += eat_a

    print(f'#{t} {candy}')