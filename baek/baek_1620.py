# 1620. 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

num_name = {}
name_num = {}

for i in range(1, N+1):
    name = input()
    num_name[i] = name
    name_num[name] = i

for _ in range(M):
    q = input()
    if q.isdecimal():
        print(num_name[int(q)])
    else:
        print(name_num[q])