# 스도쿠 검증

T = int(input())

for t in range(1, T+1):
    sudoku = [[int(x) for x in input().split()] for _ in range(9)]
    
    is_ok = True
    crit = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for i in range(9):
        check = set()
        for j in range(9):
            check.add(sudoku[i][j])
        if check != crit:
            is_ok = False
        
    for j in range(9):
        check = set()
        for i in range(9):
            check.add(sudoku[i][j])
        if check != crit:
            is_ok = False

    for i in range(3):
        for j in range(3):
            check = set()
            for k in range(9):
                check.add(sudoku[i * 3 + k // 3][j * 3 + k % 3])
            if check != crit:
                is_ok = False
    
    if is_ok:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')