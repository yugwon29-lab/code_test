# 24060. 알고리즘 수업 - 병합 정렬 1

N, K = map(int, input().split())
my_list = [int(x) for x in input().split()]
tmp = [0] * (N+1)
cnt = 0
saved_num = -1

def merge(a_list, l, mid, r):
    global cnt, saved_num

    i, j, t = l, mid + 1, 1
    while i <= mid and j <= r:
        if a_list[i] <= a_list[j]:
            tmp[t] = a_list[i]
            i += 1
        else:
            tmp[t] = a_list[j]
            j += 1
        t += 1
    while i <= mid:
        tmp[t] = a_list[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = a_list[j]
        t += 1
        j += 1
    i, t = l, 1
    while i <= r:
        a_list[i] = tmp[t]
        cnt += 1
        if cnt == K:
            saved_num = a_list[i]
        t += 1
        i += 1

def merge_sort(a_list, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(a_list, l, mid)
        merge_sort(a_list, mid + 1, r)
        merge(a_list, l, mid, r)

merge_sort(my_list, 0, N-1)

print(saved_num)
