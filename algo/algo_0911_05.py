# 장훈이의 높은 선반
T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    H = [int(x) for x in input().split()]
    
    min_height = sum(H)
    
    height_set = set([0])
    for i in range(N):
        for height in list(height_set):
            new_height = height + H[i]
            if new_height >= B:
                if min_height > new_height:
                    min_height = new_height
            else:
                height_set.add(new_height)

    print(f'#{t}', min_height - B)