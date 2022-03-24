import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if k == 1:
            print("YES")
            for i in range(1, n+1):
                print(i)
        elif n%2 == 1:
            print("NO")
        else:
            print("YES")
            for i in range(1, n+1):
                print(*[j for j in range(i, n*k+1, n)])
    

if __name__ == "__main__":
    main()
    