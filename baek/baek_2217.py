# 2217. 로프

N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

rope.sort()

ans = 0
for i in range(N):
    ans = max(ans, rope[N-1-i]*(i+1))

print(ans)