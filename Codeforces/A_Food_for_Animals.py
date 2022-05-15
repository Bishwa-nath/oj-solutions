import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        a, b, c, x, y = get_ints()
        if a+c >= x and b+c >= y and a+b+c >= x+y:
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
    