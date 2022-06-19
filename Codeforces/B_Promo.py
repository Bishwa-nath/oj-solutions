#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

# to be fixed
def main():
    n, q = get_ints()
    p = get_ls()
    p.sort()
    dp = []
    add = 0
    for i in range(n):
        add += p[i]
        dp.append(add)

    dp.reverse()

    for i in range(q):
        x, y = get_ints()
        
        print(res)
    print(dp)

        

if __name__ == "__main__":
    main()
     