T = int(input())

for test_case in range(1, T + 1):

    # 4789. 성공적인 공연 기획
    clap_people = [int(x) for x in input()]
    
    all_people = sum(clap_people)
    clapping_people = 0
    hired_people = 0

    for i, clap in enumerate(clap_people):
        # 박수!
        if i <= clapping_people:
            clapping_people += clap
        else:
            hire = i - clapping_people

            # 박수치는 사람 부족 시, 사람 고용
            hired_people += hire
            all_people += hire
            clapping_people += hire + clap

        if all_people == clapping_people:
            break

    print(f'#{test_case} {hired_people}')