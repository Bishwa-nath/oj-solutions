import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        ls = []
        for i in range(n):
            x = input()
            ls.append(x)
        
        mn = mn2 = 999999999
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                ans = 0
                for k in range(m):
                    aa = ord(ls[i][k])
                    bb = ord(ls[j][k])
                    ans += abs(aa-bb)
                mn = min(mn, ans)
            mn2 = min(mn2, mn)
        
        print(mn2)

if __name__ == "__main__":
    main()
     