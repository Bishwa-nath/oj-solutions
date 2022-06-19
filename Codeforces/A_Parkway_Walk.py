#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        a = get_ls()
        total = sum(a)
        print(max(0, total-m))
        

if __name__ == "__main__":
    main()
     
