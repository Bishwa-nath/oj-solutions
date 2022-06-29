#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        a, b, c = get_ints()
        x = a+b+c
        y  = b+c
        z = c
        print(x, y, z)
        

if __name__ == "__main__":
    main()
     