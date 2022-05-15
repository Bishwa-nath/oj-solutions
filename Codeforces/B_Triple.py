import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        a.sort()
        cnt = 1
        ans = 0
        for i in range(n-1):
            if a[i] == a[i+1]:
                cnt += 1
                if cnt >= 3:
                    ans = a[i]
                    break
            else:
                cnt = 1
        if ans:
            print(ans)
        else:
            print(-1)

if __name__ == "__main__":
    main()
    