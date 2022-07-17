#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        d = {}
        ans = 0
        for c in s:
            if c in d:
                d[c] += 1
                ans += 1
            else:
                d[c] = 1
                ans += 2
        print(ans)

if __name__ == "__main__":
    main()
     