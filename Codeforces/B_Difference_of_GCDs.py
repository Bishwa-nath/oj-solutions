#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, l, r = map(int, input().split())
        ans = []
        for i in range(1, n+1):
            temp = r//i
            temp *= i
            if l <= temp <= r:
                ans.append(temp)
                
        if len(ans) == n:
            print("YES")
            print(*ans)
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
     