import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ls.sort()
        ok = True
        for i in range(len(ls)-1):
            if ls[i] == 0 and ls[i+1] == 1:
                ok = False
                break
        #print("YES" if ok else "NO")
        if 0 in ls and 1 in ls:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
    