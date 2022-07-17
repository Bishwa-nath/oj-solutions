#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ans = []
        print(2)
        ok = [0]*(n+1)
        for i in range(1, n+1):
            if ok[i] == 0:
                j = i
                while j <= n:
                    ok[j] = 1
                    ans.append(j)
                    j *= 2

        print(*ans)

if __name__ == "__main__":
    main()
     