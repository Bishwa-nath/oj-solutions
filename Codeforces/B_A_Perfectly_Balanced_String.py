import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        n = len(s)
        st = set(s)
        ok = True
        sub_s = ''
        for i in range(n):
            if s[i] not in sub_s:
                sub_s += s[i]
            else:
                break

        mn = len(sub_s)
        if mn == n:
            print("YES")
        else:    
            j = 0
            for k in range(mn, n):
                if s[k] != s[j]:
                    ok = False
                    break
                else:
                    j += 1
            
            if len(st) == 1 or len(st) == n: ok = True
            
            print("YES" if ok else "NO")
            
    
if __name__ == "__main__":
    main()
    