import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        b = get_ls()
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                if a[i] >= a[j] and b[i] >= b[j]:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    res.append([i+1, j+1])
        
        if a == sorted(a) and b == sorted(b):
            print(len(res))
            for x in res:
                print(*x)
        else:
            print(-1)

if __name__ == "__main__":
    main()
     