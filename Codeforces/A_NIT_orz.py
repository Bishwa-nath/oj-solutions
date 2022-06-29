#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, z = get_ints()
        a = get_ls()
        for i, x in enumerate(a):
            a[i] = a[i] | z
            z = a[i] & z
        print(max(a))
        

if __name__ == "__main__":
    main()
     