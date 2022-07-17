#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        a =""
        for c in s:
            a += c.lower()
        if a == "yes":
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
     