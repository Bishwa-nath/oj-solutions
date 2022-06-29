#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        mid = n//2
        ans = 1
        for i in range(mid, 0, -1):
            if s[i-1] == s[mid]:
                ans += 1
            else:
                break
        for i in range(mid+1, n):
            if s[i] == s[mid]:
                ans += 1
            else:
                break
        
        print(ans)

if __name__ == "__main__":
    main()
     