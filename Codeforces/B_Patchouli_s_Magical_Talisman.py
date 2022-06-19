import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        even = 0
        total = 0
        ans = 0
        for x in ls:
            if x%2 == 0:
                even += 1
                total += x
        if even == n:
            while total%2 == 0:
                total /= 2
                ans += 1
            print(ans+even-1)
        
        else:
            print(min(even, ans))
            

if __name__ == "__main__":
    main()
     