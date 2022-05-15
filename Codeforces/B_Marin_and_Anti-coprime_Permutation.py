import sys
import math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        if n%2 == 1:
            print(0)
        else:
            odd = n//2;
            even = n//2;
            odd_fact = math.factorial(odd)
            even_fact = math.factorial(even)
            ans = (odd_fact*even_fact)%998244353
            print(ans)


    

if __name__ == "__main__":
    main()
    