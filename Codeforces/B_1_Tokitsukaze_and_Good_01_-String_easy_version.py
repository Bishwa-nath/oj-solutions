import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        a, b = 0, 0
        ans = 0
        for c in s:
            if c == '1':
                a += 1
                if b%2 == 1:
                    ans += 1
                    a += 1
                    b = 0
            elif c == '0':
                b += 1
                if a%2 == 1:
                    ans += 1
                    b += 1
                    a = 0
        print(ans)
        

if __name__ == "__main__":
    main()
     