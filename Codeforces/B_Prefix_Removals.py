import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else: d[c] += 1
        i = 0
        for c in s:
            if d[c] >= 2:
                d[c] -= 1
                i += 1
            else: break
        print(s[i:])

if __name__ == "__main__":
    main()
    