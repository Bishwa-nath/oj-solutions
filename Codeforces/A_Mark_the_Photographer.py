#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, x = get_ints()
        ls = get_ls()
        ok = False
        ls.sort()
        cnt = 0
        j = 0
        for i in range(n, 2*n):
            if abs(ls[i] - ls[j]) >= x:
                cnt += 1
                j += 1
                if cnt >= n:
                    ok = True

        if ok:
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
     