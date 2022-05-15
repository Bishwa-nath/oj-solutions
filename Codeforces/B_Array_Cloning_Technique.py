import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ls2 = list()
        for i in ls:
            x = ls.count(i)
            ls2.append(x)
        mx = max(ls2)
        rem = n - mx
        ans = n - mx
        while mx < n:
            ans += 1
            mx *= 2
        print(ans)

if __name__ == "__main__":
    main()
    