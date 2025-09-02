# 2668. 숫자고르기

N = int(input())
one = list(range(1, N+1))
two = list()
for _ in range(N):
    two.append(int(input()))

visited = [False] * (N+1)
max_num = 0
max_list = []

def choice_num(num_list, set_A, set_B):
    global max_num, max_list
    
    if set_A == set_B:
        if len(num_list) > max_num:
            max_num = len(num_list)
            max_list = num_list
