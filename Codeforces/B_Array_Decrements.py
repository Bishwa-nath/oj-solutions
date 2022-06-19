#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(a, b, n):
    for i in range(n):
        if a[i] < b[i]:
            return False

    diff = math.inf
    for i in range(n):
        if b[i] != 0:
            diff = min(diff, a[i] - b[i])
    
    if diff == math.inf:
        return True
    
    for i in range(n):
        if a[i] - b[i] > diff: return False
        if b[i] != 0 and a[i] - b[i] < diff: return False

    return True

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        b = get_ls()
        print("YES" if solve(a, b, n) else "NO")

if __name__ == "__main__":
    main()
     