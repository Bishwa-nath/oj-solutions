import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, k = get_ints()
        ls = get_ls()
        ans = 0
        ls.sort()
        ans = sum(ls[:n-2*k], sum(map(lambda x: ls[x+n-2*k]//ls[x+n-k], range(0, k))))
        print(ans)

        

if __name__ == "__main__":
    main()
    