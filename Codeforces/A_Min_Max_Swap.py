import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        b = get_ls()
        for i in range(n):
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]
        
        print(max(a) * max(b))
    

if __name__ == "__main__":
    main()
    