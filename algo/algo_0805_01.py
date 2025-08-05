# 백만 개의 정수 정렬

num_list = [int(x) for x in input().split()]

# 카운트 리스트
cnt = [0] * 1000001
A = [None] * len(num_list)

for num in num_list:
    cnt[num] += 1

for i in range(len(cnt)):
    if i - 1 >= 0:
        cnt[i] = cnt[i] + cnt[i-1]

for num in num_list[::-1]:
    cnt[num] = cnt[num] - 1
    A[cnt[num]] = num

print(A[500000])