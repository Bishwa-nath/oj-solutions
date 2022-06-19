#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        if n%3 == 0:
            print(n//3, n//3+1, n//3-1)
        elif n%3 == 1:
            print(n//3, n//3+2, n//3-1)
        elif n%3 == 2:
            print(n//3+1, n//3+2, n//3-1)
        

if __name__ == "__main__":
    main()
     