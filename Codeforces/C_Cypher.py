#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        for i in range(n):
            x, m = input().split()
            x = int(x)
            for c in m:
                if c == 'U':
                    ls[i] -= 1
                    if ls[i] == -1:
                        ls[i] = 9
                elif c == 'D':
                    ls[i] += 1
                    if ls[i] == 10:
                        ls[i] = 0

        print(*ls)

        

if __name__ == "__main__":
    main()
     