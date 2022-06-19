#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        a = get_ls()
        res = 0
        for x in a:
            if x > a[0]:
                res += 1
        print(res)
        

if __name__ == "__main__":
    main()
     