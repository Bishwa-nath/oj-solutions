import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        b = get_ls()
        ans = 0
        for i in range(n-1):
            ans += abs(a[i]-a[i+1])
            ans += 1
        

if __name__ == "__main__":
    main()
    