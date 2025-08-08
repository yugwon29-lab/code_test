T = int(input())

for test_case in range(1, T + 1):

    # 2383. 점심 식사시간
    
    # 입력 받기
    N = int(input())
    lunch_map = [[int(x) for x in input().split()] for _ in range(N)]

    stairs = []
    people = []

    class Stairs():
        def __init__(self, i, j, l):
            self.i, self.j = i, j
            self.people = []
            self.length = l

        def add_person(self, pi, pj):
            time = abs(self.i - pi) + abs(self.j - pj)
            self.people.append(time)

        def sort_people(self):
            self.people.sort()            
            return self.people

        def simulate(self):

            # 정렬하기
            waiting = self.sort_people()

            for i in range(len(waiting)):
                if i < 3:
                    waiting[i] += (1 + self.length)
                else:
                    if waiting[i] < waiting[i-3]:
                        waiting[i] = waiting[i-3] + self.length
                    else:
                        waiting[i] += (1 + self.length)

            return waiting[-1] if len(waiting) else None
        
        def clear(self):
            self.people.clear()

    min_time = None

    # 계단 위치 및 사람 위치 저장하기
    for i in range(N):
        for j in range(N):
            if lunch_map[i][j] >= 2:
                stairs.append(Stairs(i, j, lunch_map[i][j]))
            elif lunch_map[i][j] == 1:
                people.append((i, j))

    for case in range(len(stairs) ** len(people)):
        for j in range(len(people)):
            if (case & (1 << j)):
                stairs[1].add_person(people[j][0], people[j][1])
            else:
                stairs[0].add_person(people[j][0], people[j][1])
        
        local_max = None
        for st in stairs:
            local_time = st.simulate()
            if local_time is not None:
                if local_max is None:
                    local_max = local_time
                else:
                    if local_max < local_time:
                        local_max = local_time
            st.clear()
        
        if min_time is None:
            min_time = local_max
        else:
            if min_time > local_max:
                min_time = local_max
    
    print(f'#{test_case} {min_time}')