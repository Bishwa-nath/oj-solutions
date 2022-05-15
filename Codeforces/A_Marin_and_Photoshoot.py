import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        l = len(s)
        ans = 0
        for i in range(n-1):
            if s[i] == s[i+1] == '0':
                ans += 2
        for i in range(n-2):
            if s[i] == '0' and s[i+1] == '1' and s[i+2] == '0':
                ans += 1
        print(ans)

    

if __name__ == "__main__":
    main()
    