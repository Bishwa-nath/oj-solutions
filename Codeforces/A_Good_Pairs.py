import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        
        mx = max(ls)
        mn = min(ls)
        print(ls.index(mn)+1, ls.index(mx)+1)

if __name__ == "__main__":
    main()
    