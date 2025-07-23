T = int(input())

for test_case in range(1, T + 1):

    # 2056. 연월일 달력
    a = input()

    ok = True
    year, month, day = int(a[:4]), int(a[4:6]), int(a[6:])
    
    # 월일 체크
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            ok = False
    elif month == 2:
        if not 1 <= day <= 28:
            ok = False
    elif month in [4, 6, 9, 11]:
        if not 1 <= day <= 30:
            ok = False
    else:
        ok = False

    if ok:
        print(f"#{test_case} {year:04}/{month:02}/{day:02}")
    else:
        print(f"#{test_case} -1")