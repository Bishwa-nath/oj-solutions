#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        
        for i in range(n):
            for j in range(m):
                if i%4 == 0 or i%4 == 3:
                    if j%4 == 0 or j%4 == 3:
                        print("1 ", end='')
                    else: print("0 ", end='')
                else:
                    if j%4 == 0 or j%4 == 3:
                        print("0 ", end='')
                    else: print("1 ", end='')
            print()
        

if __name__ == "__main__":
    main()
     