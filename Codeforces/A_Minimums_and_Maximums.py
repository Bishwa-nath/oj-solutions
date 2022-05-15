import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        a, b, c, d = get_ints()
        if a==d:
            print(a)
        elif a <= c <= b:
            print(c)
        elif a < c and b < c:
            print(a+c)
        elif a>c and b>c:
            if c < d and a < d:
                print(a)
            elif c < d and a > d:
                print(a+c)
            else:
                print(a+c)

        

if __name__ == "__main__":
    main()
     