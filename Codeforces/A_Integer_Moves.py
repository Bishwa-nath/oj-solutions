import sys
import math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        x, y = get_ints()
        a = math.sqrt(x*x + y*y)
        a = math.floor(a)
        b = x*x + y*y
        if a == 0:
            print(0)
        elif a*a == b:
            print(1)
        else:
            print(2)
    

if __name__ == "__main__":
    main()
    