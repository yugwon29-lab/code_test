# 7785. 회사에 있는 사람

N = int(input())

company = {}

for _ in range(N):
    name, ent = input().split()
    if ent == 'enter':
        company[name] = True
    else:
        company[name] = False

name_list = list(company.keys())
name_list.sort(reverse=True)

for n in name_list:
    if company[n]:
        print(n)