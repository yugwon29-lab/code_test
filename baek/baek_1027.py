# 1027. 고층 건물

N = int(input())
build = [0] + [int(x) for x in input().split()]

# 보이는 고층 건물 수
watch = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        can_see = True
        for k in range(i+1, j):
            x, y = k - i, j - k
            k_height = (build[i] * y + build[j] * x) / (x + y)
            if k_height <= build[k]:
                can_see = False
        if can_see:
            watch[i] += 1
            watch[j] += 1

print(max(watch))