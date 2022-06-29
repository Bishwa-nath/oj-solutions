#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        
        ans = a[0]
        
        for x in a:
            ans ^= x
        print(ans)

if __name__ == "__main__":
    main()
     