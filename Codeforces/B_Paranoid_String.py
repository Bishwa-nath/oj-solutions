#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        ans = n
        for i in range(1, n):
            if s[i] != s[i-1]:
                ans += i
        print(ans)

if __name__ == "__main__":
    main()
     