#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        if n%2 == 1:
            print(-1)
        else:
            print(0, n//2, n//2)

if __name__ == "__main__":
    main()
     