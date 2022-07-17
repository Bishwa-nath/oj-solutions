#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, t = get_ints()
        ls = get_ls()
        cnt = 0
        for i in range(n):
            if ls[i] < t/2:
                ls[i] = 0
            elif ls[i] > t/2:
                ls[i] = 1
            else:
                ls[i] = cnt%2
                cnt += 1
        print(*ls)
        

if __name__ == "__main__":
    main()
     