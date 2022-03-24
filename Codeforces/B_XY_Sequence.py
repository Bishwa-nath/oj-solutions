import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, b, x, y = get_ints()
        a = 0
        ans = a
        for i in range(n):
            if a+x <= b:
                a += x
            else:
                a -= y
            ans += a
            
        print(ans)
        
    

if __name__ == "__main__":
    main()
    