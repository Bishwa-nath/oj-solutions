import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = []
        for i in range(2):
            x = get_ls()
            ls.append(x)

        sum1 = sum(ls[0])
        sum2 = 0
        ans = math.inf
        for  i in range(n):
            sum1 -= ls[0][i]
            ans = min(ans, max(sum1, sum2))
            sum2 += ls[1][i]

        print(ans)

if __name__ == "__main__":
    main()
     