import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        i, j = 0, n-1
        x, y = ls[0], ls[-1]
        ans = 0

        while i < j:
            if x == y:
                ans = max(ans, i+1+n-j)
            if x <= y:
                i += 1
                x += ls[i]
            else:
                j -= 1
                y += ls[j]
        
        print(ans)
        

if __name__ == "__main__":
    main()
    