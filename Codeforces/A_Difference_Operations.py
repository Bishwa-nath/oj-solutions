#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ok = True
        for i in range(1, n):
            if ls[i]%ls[0] != 0:
                ok = False
                break
        print("YES" if ok else "NO")

if __name__ == "__main__":
    main()
     