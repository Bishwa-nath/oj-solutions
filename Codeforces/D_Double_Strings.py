#!/usr/bin/env python3
import sys
import math

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))


def main():
    for _ in range(int(input())):
        n = int(input())
        ls = []
        st = set()
        for i in range(n):
            x = input()
            ls.append(x)
            st.add(x)
        
        ans = ""
        for i in range(n):
            ok = False
            temp = ls[i]
            temp_len = len(temp)
            for k in range(1, temp_len):
                if ls[i][:k] in st and ls[i][k:] in st:
                    ok = True
            if ok:
                ans += '1'
            else:
                ans += '0'
        print(ans)


if __name__ == "__main__":
    main()
     