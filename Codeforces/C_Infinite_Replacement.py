import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        t = input()
        if t == 'a':
            print(1)
        elif 'a' in t:
            print(-1)
        else:
            n = len(s)
            print(1 << n)
        

if __name__ == "__main__":
    main()
    