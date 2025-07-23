T = int(input())


class Pizza():
    def __init__(self, num, cheeze):
        self.num = num
        self.cheeze = cheeze

    def melted(self):
        self.cheeze = self.cheeze // 2

    def IsDone(self):
        return self.cheeze == 0


for test_case in range(1, T + 1):

    # 5099. 피자 굽기
    N, M = map(int, input().split())
    C = [int(x) for x in input().split()]
    pizza = [Pizza(x, C[x-1]) for x in range(1, M+1)]

    # 화덕 queue 생성
    p_queue = []

    # 처음 N개의 피자 넣기
    for i in range(N):
        p = pizza.pop(0)
        p_queue.append(p)

    while p_queue or pizza:
        p_queue[0].melted()
        if p_queue[0].IsDone():
            last_pizza = p_queue.pop(0)
            last_pizza_num = last_pizza.num
            if pizza:
                p_queue.append(pizza.pop(0))
        else:
            p_queue.append(p_queue.pop(0))

    print(f'#{test_case} {last_pizza_num}')
