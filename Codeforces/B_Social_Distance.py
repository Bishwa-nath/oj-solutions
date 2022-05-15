import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))
# Baaaaaallllllll
def main():
    for _ in range(int(input())):
        n, m = get_ints()
        ls = get_ls()
        res = 0
        for x in ls:
            res += x
        res = res - min(ls) + max(ls) + n

        if n > m or res > m:
            print("NO")
        else:
            print("YES")
        

if __name__ == "__main__":
    main()
    