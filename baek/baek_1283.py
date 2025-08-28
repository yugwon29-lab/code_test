# 1283. 단축키 지정
N = int(input())
options = [input().split() for _ in range(N)]

shortkey = set()

for i in range(N):
    opt = options[i]
    # 1번 규칙
    rule_1 = False
    for j in range(len(opt)):
        word = opt[j].upper()
        if word[0] not in shortkey:
            rule_1 = True
            shortkey.add(word[0])
            options[i][j] = "[" + opt[j][0] + "]" + opt[j][1:]
            break
    # 2번 규칙
    rule_2 = False
    if not rule_1:
        for j in range(len(opt)):
            word = opt[j].upper()
            for k in range(1, len(word)):
                if word[k] not in shortkey:
                    rule_2 = True
                    shortkey.add(word[k])
                    options[i][j] = opt[j][:k] + "[" + opt[j][k] + "]" + opt[j][k+1:]
                    break
            
            if rule_2:
                break

for opt in options:
    print(*opt)