#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        ans = 0
        for i in range(1, n+1):
            ans += i*m
            
        for i in range(m):
            ans += i
        print(ans)
        

if __name__ == "__main__":
    main()
     