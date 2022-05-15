import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def sol():
    n = int(input())
    a = get_ls()
    b = get_ls()
    c = 0
    d = list()
    d.append(0)
    ok = True
    for i in range(n):
        x = b[i] - a[i]
        if x < 0: return False
        d.append(x)
    d.append(0)
    for i in range(len(d)-1):
        if d[i] != d[i+1]:
            c += 1
    return (c <= 2)

def main():
    for _ in range(int(input())):
        if sol():
            print("YES")
        else:
            print("NO")
    

if __name__ == "__main__":
    main()
    