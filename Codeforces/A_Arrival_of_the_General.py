#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n = int(input())
    ls = list(map(int, input().split()))
    mx = max(ls)
    mn = min(ls[::-1])
    ans = 0
    ans += ls.index(mx)
    ans += ls[::-1].index(mn)
    print(ans - (ans >= n))

        

if __name__ == "__main__":
    main()
     