# 11047.동전 0
N, K = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))

# 사용한 동전의 개수
num = 0

# 큰 동전부터 쓰자. (그리디)
for i in range(N-1, -1, -1):
    if K == 0:
        break
    num += K // A[i]
    K = K % A[i]

# 최대 동전 수 출력
print(num)