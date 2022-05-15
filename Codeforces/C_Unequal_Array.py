import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        eq = 0
        
        for i in range(n-1):
            if ls[i] == ls[i+1]:
                eq += 1

        a, b = 0, 0
        for i in range(n-1):
            if ls[i] == ls[i+1]:
                a = i+1
                break
        for i in range(n-1, 1, -1):
            if ls[i] == ls[i-1]:
                b = i-1
                break

        df = b - a
        if df==0: df += 1
        print(0 if eq <= 1 else df)
        

if __name__ == "__main__":
    main()
    