T = int(input())

for test_case in range(1, T + 1):

    # 1974. 스도쿠 검증
    sudoku = [[int(x) for x in input().split()] for i in range(9)]

    valid = True

    # 가로줄 체크
    if valid:
        for i in range(9):
            check = []
            for v in sudoku[i]:
                if v in check:
                    valid = False
                    break
                else:
                    check.append(v)
    
    # 세로줄 체크
    if valid:
        for i in range(9):
            check = []
            for v in [sudoku[a][i] for a in range(9)]:
                if v in check:
                    valid = False
                    break
                else:
                    check.append(v)

    # 3x3 체크
    if valid:
        for i in range(3):
            for j in range(3):
                check = []
                for v in [sudoku[a][b] for a in range(i*3, i*3+3) for b in range(j*3, j*3+3)]:
                    if v in check:
                        valid = False
                        break
                    else:
                        check.append(v)

    if valid:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

    

