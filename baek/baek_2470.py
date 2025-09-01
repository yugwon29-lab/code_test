# 2470. 두 용액
N = int(input())

solution = [int(x) for x in input().split()]

solution.sort()

a, b = 0, N-1
min = abs(solution[a] + solution[b])
ma, mb = a, b

while a < b:
    shake = solution[a] + solution[b]
    if min <= abs(shake):
        if shake > 0:
            b -= 1
        elif shake < 0:
            a += 1
        else:
            ma, mb = a, b
            break
    else:
        min = abs(shake)
        ma, mb = a, b
        if shake > 0:
            b -= 1
        elif shake < 0:
            a += 1
        else:
            ma, mb = a, b
            break

print(solution[ma], solution[mb])