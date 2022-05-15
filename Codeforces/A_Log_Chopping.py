import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        s = 0
        for x in ls:
            s += (x-1)
        
        if s%2 == 1:
            print('errorgorn')
        else:
            print('maomao90')
        

if __name__ == "__main__":
    main()
    