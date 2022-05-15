import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ls.sort()
        ok = True
        for i in range(1, n-1):
            a = abs(ls[i] - ls[i-1])
            b = abs(ls[i+1] - ls[i])
            if a != 2*b and b != 2*a:
                ok = False
                break

        print("Yes" if ok else "No")

if __name__ == "__main__":
    main()
    