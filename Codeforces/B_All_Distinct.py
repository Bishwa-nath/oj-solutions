#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        d = dict()
        for x in a:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        ln = len(d)
        rem = 0
        for x in d.values():
            if  x>1:
                rem += (x-1)
        if rem%2 == 1:
            rem += 1
        if ln == n:
            print(n)
        else:
            print(n-rem)
        

if __name__ == "__main__":
    main()
     