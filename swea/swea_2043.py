# 2043.서랍의 비밀번호

P, K = map(int, input().split())

num = P - K
if num < 0:
    num = 1000 - num
else:
    num = num + 1

print(num)