# 11726. 2xn 타일링

N = int(input())

# 테이블 설정
d = [0] * (N+2)

# 초기값 설정
d[1] = 1
d[2] = 2

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N]%10007)