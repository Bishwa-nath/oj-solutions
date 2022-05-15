import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        ok = True
        if len(s) == 1:
            print("NO")
        else:
            n = len(s)
            
            a, b = 0, 0
            for i in range(n):
                if s[i] == 'A':
                    a += 1
                else:
                    b += 1
                    if a >= b:
                        a -= 1
                        b -= 1
                    else:
                        ok = False
                        break
            if s[-1] == 'A': ok = False
            if a == n and b == 0: ok = False
            print("YES" if ok else "NO")
        

if __name__ == "__main__":
    main()
    