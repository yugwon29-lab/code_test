# 14425. 문자열 집합
N, M = map(int, input().split())

# 변수 집합
ROOT = 1
unused = 2

MX = 10000 * 500 + 5

chk = [False] * MX
nxt = [[-1] * 26 for _ in range(MX)]

# 문자를 정수로
def c2i(s):
    return ord(s) - ord('a')

# 삽입 함수
def insert(s):
    global unused
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            nxt[cur][c2i(c)] = unused
            unused += 1
        cur = nxt[cur][c2i(c)]
    chk[cur] = True

# 찾기 함수
def find(s):
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            return False
        cur = nxt[cur][c2i(c)]
    return chk[cur]

# 삭제 함수 (사실 이 문제에서 필요 없음)
def erase(s):
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            return
        cur = nxt[cur][c2i(c)]
    chk[cur] = False

# 문자열 삽입
for i in range(N):
    insert(input())

# 문자열 검색
cnt = 0
for j in range(M):
    if find(input()):
        cnt += 1

print(cnt)