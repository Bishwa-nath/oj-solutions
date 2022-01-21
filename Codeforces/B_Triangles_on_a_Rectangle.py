t = int(input())

for i in range(t):
    w, h = map(int, input().split())
    res = 0
    for _ in range(4):
        ls = [int(x) for x in input().split()][1:]
        res = max(res, (ls[-1] - ls[0]) * ( w if _ > 1 else h))

    print(res)