import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n = int(input())
    ls = get_ls()
    ans = 0
    x = list()
    for i in ls:
        ans = 0
        while i < 32768:
            i *= 2
            ans += 1
        print(i)
        x.append(ans)
    print(*x)

if __name__ == "__main__":
    main()
    