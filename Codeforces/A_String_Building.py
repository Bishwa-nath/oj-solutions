import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        ok = True
        if len(s) == 1:
            print("NO")
        elif len(s) == 2:
            if s == 'ab' or s == 'ba':
                print("NO")
            else:
                print("YES")
        else:
            for i in range(len(s)-3):
                if s[i:i+3] == 'aba' or s[i:i+3] == 'bab':
                    ok = False
            if s[:2] == 'ab' or s[:2] == 'ba':
                ok = False
            if s[-2:] == 'ab' or s[-2:] == 'ba':
                ok = False
            print("YES" if ok else "NO")
        

if __name__ == "__main__":
    main()
    