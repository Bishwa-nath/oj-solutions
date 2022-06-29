#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        ans = 0
        found = False

        for x in a:
            if x > 0:
                found = True
            else:
                if found:
                    ans += 1
                found = False
        if found:
            ans += 1
        if ans > 2:
            print(2)
        else:
            print(ans)

if __name__ == "__main__":
    main()
     