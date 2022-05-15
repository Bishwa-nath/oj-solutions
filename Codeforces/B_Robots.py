import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        ls = []
        ok = True
        for i in range(n):
            x = input()
            ls.append(x)
        
        a, b = 0, 0
        found = False
        for i in range(n):
            for j in range(m):
                if ls[i][j] == 'R':
                    a = i
                    b = j
                    found = True
                    break
            if found: break
        
        for i in range(a+1, n):
            for j in range(b):
                if ls[i][j] == 'R':
                    ok = False
                    break
        
        print("YES" if ok else "NO")
        
        

if __name__ == "__main__":
    main()
     