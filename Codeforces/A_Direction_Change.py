import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))
# Baaaaaaaaaaallllllll
def main():
    for _ in range(int(input())):
        n, m = get_ints()
        if n < m:
            n, m = m, n
        if m == 1 and n > 2:
            print(-1)
        else:
            print(n*2-2-(n+m)%2)
        

if __name__ == "__main__":
    main()
    