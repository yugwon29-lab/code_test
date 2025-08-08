T = int(input())

for test_case in range(1, T + 1):

    # 2382. 미생물 격리
    
    # 입력 받기
    N, M, K = map(int, input().split())

    movement = {
        1 : (-1, 0), 2 : (1, 0), 3 : (0, -1), 4 : (0, 1)
    }

    class Gem():
        def __init__(self, i, j, num, move_num):
            self.i, self.j = i, j
            self.num = num
            self.movement = movement[move_num]
        
        def move(self):
            self.i, self.j = self.i + self.movement[0], self.j + self.movement[1]

            # 셀 가장자리 도달 시
            if self.i == 0 or self.i == N - 1 or self.j == 0 or self.j == N - 1:
                # 군집 내 미생물 절반이 죽는다.
                self.num = self.num // 2
                # 이동 방향이 바뀐다.
                self.movement = (-self.movement[0], -self.movement[1])

    def merge_gem(gems):
        gi, gj = gems[0].i, gems[0].j
        sum_gem = 0
        max_num = 0
        max_movement = -1
        for g in gems:
            sum_gem += g.num
            if max_num < g.num:
                max_num = g.num
                max_movement = g.movement
        
        for k in movement.keys():
            if movement[k] == max_movement:
                max_movement = k
     
        return Gem(gi, gj, sum_gem, max_movement)
            

    gem_list = []

    # 군집 입력
    for i in range(K):
        gi, gj, gn, gm = map(int, input().split())
        gem_list.append(Gem(gi, gj, gn, gm))

    m = 0
    while m < M:
        gem_dict = {}

        # 1시간이 지나며 모든 군집이 이동한다.
        for g in gem_list:
            g.move()
            if g.num != 0:
                gem_dict[(g.i, g.j)] = gem_dict.get((g.i, g.j), list()) + [g]

        gem_list.clear()
        
        # 위치가 겹친 군집을 찾는다.
        for k in gem_dict.keys():
            if len(gem_dict[k]) > 1:
                gem_list.append(merge_gem(gem_dict[k]))
            else:
                gem_list.append(gem_dict[k][0])
        
        m += 1

    num_gem = 0
    for g in gem_list:
        num_gem += g.num

    print(f'#{test_case} {num_gem}')
