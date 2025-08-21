# 12852. 1로 만들기 2

N = int(input())

# 테이블 정의
d = [0] * (N+1)
bf = [0] * (N+1)
# D[i] = i를 1로 만드는데 필요한 최솟값

# 초기값 설정
d[1] = 0
bf[1] = 1

for i in range(2, N+1):
    d[i] = d[i-1] + 1
    bf[i] = i-1
    if i % 2 == 0:
        if d[i] >= d[i//2]+1:
            d[i] = d[i//2] + 1
            bf[i] = i//2
    if i % 3 == 0:
        if d[i] >= d[i//3]+1:
            d[i] = d[i//3] + 1
            bf[i] = i//3

print(d[N])
k = N
print(k, end=' ')
while True:
    if k == 1:
        break
    k = bf[k]
    print(k, end=' ')
    
print()
