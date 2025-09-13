# 28420. 카더가든
N, M = map(int, input().split())
a, b, c = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(N)]

min_value = None
# 가로로 연결하는 경우
for i in range(N-a+1):
    for j in range(M-(b+c)+1):
        value = 0
        # 범위의 합
        for m in range(a):
            for n in range((b+c)):
                value += board[i+m][j+n]

        if min_value is None:
            min_value = value
        else:
            min_value = min(min_value, value)

# ㄱ으로 연결하는 경우 1
for i in range(N-(a+b)+1):
    for j in range(M-(a+c)+1):
        value = 0
        # 캠핑카
        for m in range(a):
            for n in range(c):
                value += board[i+m][j+n]
        
        # 차
        for m in range(b):
            for n in range(a):
                value += board[i+a+m][j+c+n]

        if min_value is None:
            min_value = value
        else:
            min_value = min(min_value, value)

# ㄱ으로 연결하는 경우 2
for i in range(N-(a+c)+1):
    for j in range(M-(a+b)+1):
        value = 0
        # 차
        for m in range(a):
            for n in range(b):
                value += board[i+m][j+n]
        
        # 캠핑카
        for m in range(c):
            for n in range(a):
                value += board[i+a+m][j+b+n]

        if min_value is None:
            min_value = value
        else:
            min_value = min(min_value, value)

print(min_value)