T = int(input())

for i in range(1, T + 1):

    # 4843. 특별한 정렬
    N = int(input())
    a = [int(x) for x in input().split()]
    b = []

    find_max = True
    while len(b) != N:
        for n in range(len(a)):
            if n == 0:
                tmp = a[n]
            else:
                if find_max:
                    if tmp < a[n]:
                        tmp = a[n]
                else:
                    if tmp > a[n]:
                        tmp = a[n]

        find_max = not find_max
        b.append(tmp)
        a.remove(tmp)

    print(f"#{i}", end=" ")
    for n in range(10):
        if n == 9:
            print(b[n])
        else:
            print(b[n], end=" ")