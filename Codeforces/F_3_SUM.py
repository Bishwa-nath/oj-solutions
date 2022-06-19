#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        d = dict()
        ls = []
        for x in a:
            mod = x%10
            if mod in d:
                d[mod] += 1
            else:
                d[mod] = 1
            if d[mod] <= 4:
                ls.append(mod)

        ls.sort()
        ln = len(ls)
        ok = False
        for i in range(ln-2):
            for j in range(i+1, ln-1):
                for k in range(j+1, ln):
                    add = ls[i] + ls[j] + ls[k]
                    if add%10 == 3:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                break

        #print(ls)
        print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
     