import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        if len(s) == 1: print("YES")
        elif len(s) == 2 and s[0] != s[1]:
            print("YES")
        else: print("NO")
    

if __name__ == "__main__":
    main()
    