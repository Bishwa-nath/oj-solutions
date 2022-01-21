import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        ls = get_ls()
        print(max(ls) - min(ls))
        

if __name__ == "__main__":
    main()