#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        p = get_ls()
        ls = []
        for i in range(n):
            if i != p[i]:
                ls.append(i)
        res = ls[0]
        for x in ls:
            res = res & x

        print(res)

if __name__ == "__main__":
    main()
     