T = int(input())

for test_case in range(1, T + 1):

    # 2029. 몫과 나머지 출력하기
    A, B = map(int, input().split())

    print(f"#{test_case} {A//B} {A%B}")