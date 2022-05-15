import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        p = n-1
        while p > 0 and ls[p] <= ls[p-1]:
            p -= 1
        while p > 0 and ls[p] >= ls[p-1]:
            p -= 1
        print(p)

if __name__ == "__main__":
    main()
    