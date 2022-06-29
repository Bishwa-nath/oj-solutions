#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, k = get_ints()
        a = get_ls()
        ans = 0
        for i in range(1, n-1):
            if a[i] > a[i-1] + a[i+1]:
                ans += 1
        
        if k == 1:
            n = n-1
            res = n//2
            print(max(res, ans))
        else:
            print(max(ans, 0))

        

if __name__ == "__main__":
    main()
     