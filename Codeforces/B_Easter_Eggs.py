import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n = int(input())
    s = "ROY" + "GBIV"*25
    print(s[:n])

if __name__ == "__main__":
    main()