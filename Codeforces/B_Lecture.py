import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n, m = get_ints()
    d = dict()
    for _ in range(m):
        a, b = input().split()
        d[a] = b
    ls = list(input().split())
    for s in ls:
        mn = min(s, d[s], key=len)
        print(mn, end=' ')
        

if __name__ == "__main__":
    main()
    