T = int(input())

for test_case in range(1, T + 1):

    # 4008. 숫자 만들기
    D, W, K = map(int, input().split())
    flim = [[int(x) for x in input().split()] for _ in range(D)]

    def check_flim(flim):
        for x in range(W):
            test_pass = False
            for y in range(D-K+1):
                check = flim[y][x]
                test = True
                for i in range(1, K):
                    if check != flim[y+i][x]:
                        test = False
                if test:
                    test_pass = True
                    break
            if not test_pass:
                break

        return test_pass
    
    min_cnt = None

    def test_flim(cur, flim, cnt_chem=0):
        global min_cnt

        # 가지치기
        if min_cnt is not None and cnt_chem >= min_cnt:
            return

        if cur == D:
            if check_flim(flim):
                if min_cnt is None or cnt_chem < min_cnt:
                    min_cnt = cnt_chem
            return
        
        original = flim[cur][:]

        test_flim(cur+1, flim, cnt_chem)

        # A로 약품처리
        flim[cur] = [0] * W
        test_flim(cur+1, flim, cnt_chem+1)
        
        # B로 약품처리
        flim[cur] = [1] * W
        test_flim(cur+1, flim, cnt_chem+1)

        flim[cur] = original

    test_flim(0, flim, 0)

    print(f'#{test_case} {min_cnt}')