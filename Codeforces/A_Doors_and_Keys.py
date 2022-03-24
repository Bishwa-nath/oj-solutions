import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        r=0
        g=0
        b=0
        R=0
        G=0
        B=0
        for i in range(len(s)):
            if s[i] == 'r': r = i
            if s[i] == 'g': g = i
            if s[i] == 'b': b = i
            if s[i] == 'R': R = i
            if s[i] == 'G': G = i
            if s[i] == 'B': B = i
        if r < R and g < G and b < B:
            print("YES")
        else: print("NO")

    

if __name__ == "__main__":
    main()
    