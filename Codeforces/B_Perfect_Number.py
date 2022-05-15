import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def sol(x):
    s = 0
    while x > 0:
        s += x%10
        x //= 10
    return s

def main():
    ans = 18
    n = int(input())
    while n:
        ans += 1
        if sol(ans) == 10:
            n -= 1
    print(ans)

    
        

if __name__ == "__main__":
    main()
    