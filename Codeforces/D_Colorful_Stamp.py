import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        s = s.split('W')
        ok = False
        for x in s:
            a = 'R' in x
            b = 'B' in x
            if a^b:
                ok = True
                
        print("NO" if ok else "YES")
        

if __name__ == "__main__":
    main()
    