# 이진수2
T = int(input())

for t in range(1, T+1):
    F = float(input())

    to_bin = []
    while F != 0.0:
        F *= 2
        if F >= 1:
            to_bin.append('1')
            F -= 1
        else:
            to_bin.append('0')
        if len(to_bin) >= 13:
            break
    
    print(f'#{t}', end=' ')
    if len(to_bin) >= 13:
        print('overflow')
    else:
        print(''.join(to_bin))
    
    