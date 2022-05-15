import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        ok = True
        t = []
        d = dict()
        x, y = 0, 0
        if n == 1:
            print("YES")
        elif n == 2:
            if ls[1] - ls[0] > 3:
                print("NO")
            else:
                print("YES")
        else:
            for i in range(n-1):
                df = ls[i+1] - ls[i]
                if df==2: x += 1
                if df==3: y += 1 
                if df > 3: ok = False
            if not ok or x > 2 or y > 1 or (x>0 and y>0):
                print("NO")
            else:
                print("YES")
        

if __name__ == "__main__":
    main()
    