for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    cnt = 1
    if k > (n+1)//2:
        print(-1)
    else:
        for i in range(n):
            for j in range(n):
                if i == j and i%2 == 0 and cnt <= k:
                    print('R', end='')
                    cnt += 1
                else: print('.', end='')
            print()

