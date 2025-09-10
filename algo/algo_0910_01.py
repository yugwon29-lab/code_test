# 숫자를 정렬하자 (병합 정렬)
# T = int(input())

# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     else:
#         mid = len(arr) // 2
#         front = merge_sort(arr[:mid])
#         back = merge_sort(arr[mid:len(arr)])
#         new_arr = []
#         l, r = 0, 0
#         while l < len(front) and r < len(back):
#             if front[l] <= back[r]:
#                 new_arr.append(front[l])
#                 l += 1
#             else:
#                 new_arr.append(back[r])
#                 r += 1
#         while l < len(front):
#             new_arr.append(front[l])
#             l += 1
#         while r < len(back):
#             new_arr.append(back[r])
#             r += 1

#         return new_arr

# for t in range(1, T+1):
#     N = int(input())
#     numbers = [int(x) for x in input().split()]

#     result = merge_sort(numbers)
#     print(f'#{t}', *result)

# 숫자를 정렬하자 (퀵 정렬)
T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = [int(x) for x in input().split()]

    def partition(lft, rgt):
        global numbers

        pivot = numbers[lft]
        i = lft
        j = rgt
        
        while i < j:
            while i <= rgt and numbers[i] <= pivot:
                i += 1
            
            while numbers[j] > pivot:
                j -= 1

            if i < j:
                numbers[i], numbers[j] = numbers[j], numbers[i]
        
        numbers[lft], numbers[j] = numbers[j], numbers[lft]

        return j
    
    def quick_sort(lft, rgt):
        if lft < rgt:
            sorted_idx = partition(lft, rgt)

            quick_sort(lft, sorted_idx - 1)
            quick_sort(sorted_idx + 1, rgt)

    quick_sort(0, N-1)

    print(f'#{t}', *numbers)

