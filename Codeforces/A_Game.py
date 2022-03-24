import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        l = 0
        r = 0
        for i in range(len(ls)):
            if(ls[i] == 0):
                l = i-1
                break
        for i in range(len(ls)-1, 0, -1):
            if(ls[i] == 0):
                r = i+1
                break
        print(r-l)
    

if __name__ == "__main__":
    main()
    