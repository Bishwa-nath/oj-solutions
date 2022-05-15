import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        points = (n-1)*3
        p = ((n-1)//2)*3
        if n == 2:
            print(3)
        else:
            print(points-p)

if __name__ == "__main__":
    main()
    