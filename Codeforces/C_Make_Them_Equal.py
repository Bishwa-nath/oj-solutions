import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, c = input().split()
        n = int(n)
        s = input()
        if s.count(c) == n:
            print(0)
            continue
        for i in range(n//2, n):
            if s[i] == c:
                print(1)
                print(i+1)
                break
        else:
            print(2)
            print(n, n-1)

        

if __name__ == "__main__":
    main()
     