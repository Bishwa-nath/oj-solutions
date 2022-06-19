#!/usr/bin/env python3
 
import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))
 
def main():
    for _ in range(int(input())):
        a, b = get_ints()
        if a > b:
            dif = a - b
            print("01"* b + '0'*dif)
        else:
            dif = b - a
            print("10" * a + "1"*dif)
        
 
if __name__ == "__main__":
    main()
     