#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        if s.count('9') == n:
            for i in range(n-1):
                print('1', end='')
            print('2')
        elif s[0] == '9':
            temp = '1' * (n+1)
            res  = int(temp) - int(s)
            print(res)
        else:
            for i in range(n):
                print(9 - int(s[i]), end='')
            print()

if __name__ == "__main__":
    main()
     