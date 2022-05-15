import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if ls[i] >= ls[j]:
                    ans += 1
        
        print(ans)
        

if __name__ == "__main__":
    main()
     