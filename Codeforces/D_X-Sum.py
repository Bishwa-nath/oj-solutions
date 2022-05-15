import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        ar = []
        for i in range(n):
            x = get_ls()
            ar.append(x)
        ans = 0
        mx = 0
        for i in range(n):
            for j in range(m):
                a = i+1
                c = j+1
                ans = ar[i][j]
                while a < n and c < m:
                    ans += ar[a][c]
                    a += 1
                    c += 1
                a = i-1
                c = j+1
                while a >= 0 and c < m:
                    ans += ar[a][c]
                    a -= 1
                    c += 1
                a = i+1
                c = j-1
                while a < n and c >= 0:
                    ans += ar[a][c]
                    a += 1
                    c -= 1
                
                a = i-1
                c = j-1
                while a >= 0 and c >= 0:
                    ans += ar[a][c]
                    a -= 1
                    c -= 1
                mx = max(mx, ans)

        print(mx)

        

if __name__ == "__main__":
    main()
     