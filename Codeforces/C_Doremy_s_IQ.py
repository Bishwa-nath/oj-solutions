#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, q = get_ints()
        ans = [0] * n
        ls = get_ls()
        m = 0

        for i in range(n-1, -1, -1):  
            if ls[i] <= m:
                ans[i] = 1
            elif m < q:
                ans[i] = 1
                m += 1
        
        for c in ans:
            print(c, end='')
        print()
        

if __name__ == "__main__":
    main()
     