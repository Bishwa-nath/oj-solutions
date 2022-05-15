import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ans = 0
        mn = min(ls)
        for i in ls:
            ans += (i-mn)
        print(ans)
        

if __name__ == "__main__":
    main()
     