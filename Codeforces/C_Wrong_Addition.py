import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    a, s = get_ints()
    ls = []
    while s:
        x = a%10
        y = s%10
        if x <= y:
            ls.append(y-x)
        else:
            s //= 10
            y += 10 * (s%10)
            if x < y and y >= 10 and y < 19:
                ls.append(y-x)
            else:
                print(-1)
                return
        s //= 10
        a //= 10

    if a:
        print(-1)
    else:
        while True:
            if ls[-1] == 0:
                ls.pop()
            else:
                break
        ls.reverse()
        print(''.join([str(i) for i in ls]))
        

def main():
    for _ in range(int(input())):
        solve()
        

if __name__ == "__main__":
    main()
     