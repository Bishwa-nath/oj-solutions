#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ind = 0
        ans = sum(ls) - ls[-1]
        
        for i in range(n):
            if ls[i] > 0:
                ind = i
                break

        for i in range(ind, n-1):
            if ls[i] == 0:
                ans += 1
        if ls.count(0) == n:
            print(0)
        else:
            print(ans)
        

if __name__ == "__main__":
    main()
     