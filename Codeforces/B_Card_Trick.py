import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        m = int(input())
        b = get_ls()
        sum_b = sum(b)
        mod = sum_b%n
        print(a[mod])
        

if __name__ == "__main__":
    main()
     