import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        
        odd = list()
        even = list()
        for i in range(n):
            if i%2 == 0:
                even.append(a[i])
            if i%2 == 1:
                odd.append(a[i])

        ok = True
        for i in range(len(even)-1):
            if even[i]%2 != even[i+1]%2:
                ok = False
        for i in range(len(odd)-1):
            if odd[i]%2 != odd[i+1]%2:
                ok = False
        if ok:
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
    