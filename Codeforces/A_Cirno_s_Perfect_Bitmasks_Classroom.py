import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        for i in range(1, 1000000000):
            if n & i > 0 and n ^ i > 0:
                print(i)
                break

if __name__ == "__main__":
    main()
     