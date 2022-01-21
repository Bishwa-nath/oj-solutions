import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    for i in range(t):
        a, b, c = get_ints()
        x = 2*b - c
        y = 2*b - a
        z = a+c
        if (x%a == 0 and x > 0) or (y%c == 0 and y > 0) or (z%(2*b) == 0):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()