import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ok = False
        for i in range(n-1, 0, -1):
            add = int(s[i]) + int(s[i-1])
            
            if add > 9:
                print(s[:i-1] + str(add) + s[i+1:])
                ok = True
                break

        if not ok:
            print(str(int(s[0])+int(s[1])) + s[2:])

if __name__ == "__main__":
    main()
    