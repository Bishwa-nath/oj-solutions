#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        ls = []
        for i in range(2):
            a = get_ls()
            ls.append(a)
        one = 0
        for i in range(2):
            for j in range(2):
                if ls[i][j] == 1:
                    one += 1
        if one == 4:
            print(2)
        elif one == 0:
            print(0)
        else:
            print(1)
        

if __name__ == "__main__":
    main()
     