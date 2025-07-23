T = int(input())

for test_case in range(1, T + 1):

    # 4880. 토너먼트 카드게임
    N = int(input())
    cards = [int(x) for x in input().split()]

    def rsp(a, b):
        # 1: 가위, 2: 바위, 3: 보
        if cards[a] == cards[b]:
            # 무승부인 경우, 번호가 작은 쪽이 우승
            if a < b:
                return a
            else:
                return b
        else:
            if cards[a] == 1:
                if cards[b] == 2:
                    return b
                else:
                    return a
            elif cards[a] == 2:
                if cards[b] == 1:
                    return a
                else:
                    return b
            elif cards[a] == 3:
                if cards[b] == 1:
                    return b
                else:
                    return a
                
    def tournament(student):
        # student : 학생 번호들로 구성된 list
        # return : 그 그룹의 최종 승리자 번호
        if len(student) == 1:
            # 혼자 있는 그룹이면 부전승
            return student[0]
        elif len(student) == 2:
            # 두 명 있는 그룹은 대결 실행
            return rsp(student[0], student[1])
        else:
            # 그 이상이면 그룹 더 나누기
            crit = (len(student) - 1) // 2
            group_a = student[:crit+1]
            group_b = student[crit+1:]
            group_a = tournament(group_a)
            group_b = tournament(group_b)
            return rsp(group_a, group_b)
    
    student = [x for x in range(0, N)]

    print(f"#{test_case} {tournament(student)+1}")
