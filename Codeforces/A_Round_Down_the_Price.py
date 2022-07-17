#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        temp = 1
        while temp <= n:
            temp *= 10
        print(n - (temp//10))

if __name__ == "__main__":
    main()
     