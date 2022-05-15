import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        z = 0
        st = set(ls)
        for i in ls:
            if i == 0:
                z += 1

        if z > 0:
            print(n-z)
        elif len(st) == n:
            print(n+1)
        else:
            print(n)

        

if __name__ == "__main__":
    main()
     