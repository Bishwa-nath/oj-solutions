import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    for _ in range(t):
        ls = get_ls()
        a = ls[0]
        b = ls[6] - ls[4]
        c = ls[6] - (a+b)
        print(a, b, c)

if __name__ == "__main__":
    main()
    