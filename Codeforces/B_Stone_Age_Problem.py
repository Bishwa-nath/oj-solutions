#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n, q = get_ints()
    a = get_ls()
    d = {}
    res = 0
    default = 0
    for i, x in enumerate(a):
        d[i] = x
    res = sum(d.values())
    
    for _ in range(q):
        p = get_ls()
        if p[0] == 2:
            res = n*p[1]
            d = {}
            default = p[1]
        else:
            res -= d.get(p[1]-1, default)
            res += p[2]
            d[p[1]-1] = p[2]

        print(res)

if __name__ == "__main__":
    main()
     