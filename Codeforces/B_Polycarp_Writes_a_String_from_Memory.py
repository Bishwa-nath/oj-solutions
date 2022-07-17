#!/usr/bin/env python3

import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        st = set()
        ans = 0
        for c in s:
            st.add(c)
            if len(st) > 3:
                ans += 1
                st.clear()
                st.add(c)
        if len(st) > 0:
            ans += 1

        print(ans)
            

if __name__ == "__main__":
    main()
     