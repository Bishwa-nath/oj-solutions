import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        a.sort()
        sum_all = sum(a)
        avg1 = sum_all/n
        ok = False
        for x in a:
            if avg1 == x:
                ok = True
                break
        
        print("YES" if ok else "NO")
        

if __name__ == "__main__":
    main()
     