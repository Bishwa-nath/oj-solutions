import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = ""
        s = input().split()
        ans += s[0][0]
        ok = False
        for i in range(len(s)-1):
            if s[i][1] != s[i+1][0]:
                ans += s[i][1]
                ans += s[i+1][0]
                ok = True
            else: ans += s[i][1]
        
        if ok: ans += s[len(s)-1][1]
        else:
            ans += s[len(s)-1]
        print(ans)

if __name__ == "__main__":
    main()