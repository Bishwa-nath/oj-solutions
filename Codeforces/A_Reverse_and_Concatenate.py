import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        r = s[::-1]
        if k == 0 or s == r:
            print(1)
        else: print(2)
    

if __name__ == "__main__":
    main()
    