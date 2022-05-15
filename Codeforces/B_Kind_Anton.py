import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def sol():
    n = int(input())
    a = get_ls()
    b = get_ls()
    x, y = 0, 0
    for i in range(n):
        if a[i] > b[i] and not x:
            print("NO")
            return
        elif a[i] < b[i] and not y:
            print("NO")
            return
        if a[i] == -1: x = 1
        if a[i] == 1: y = 1
    print("YES")
    

def main():
    for _ in range(int(input())):
        sol()
    

if __name__ == "__main__":
    main()
    