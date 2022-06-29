#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))


def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        a.sort()
        ok = True
        zero = 0
        neg = 0
        pos = 0
        for x in a:
             if x < 0: neg += 1
             elif x > 0: pos += 1
             else: zero += 1
        if neg > 2 or pos > 2: ok = False

        x = 2
        y = 2
        z = 2
        ls = []
        for i in a:
            if i < 0 and x >= 0 :
                ls.append(i)
                x -= 1
            elif i > 0 and y >= 0:
                ls.append(i)
                y -= 1
            elif z >= 0:
                ls.append(i)
                z -= 1
        
        ls_len = len(ls)
        for i in range(ls_len-2):
            for j in range(i+1, ls_len-1):
                for k in range(j+1, ls_len):
                    add = ls[i] + ls[j] + ls[k]
                    if add not in a:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break


        print("YES" if ok else "NO")

if __name__ == "__main__":
    main()
     