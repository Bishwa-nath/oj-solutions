import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        res = ''.join(sorted(s))
        print(res)

if __name__ == "__main__":
    main()
    