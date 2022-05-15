import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        if n <= 1399:
            print("Division 4")
        elif n <= 1599:
            print("Division 3")
        elif n <= 1899:
            print("Division 2")
        else:
            print("Division 1")

if __name__ == "__main__":
    main()
    