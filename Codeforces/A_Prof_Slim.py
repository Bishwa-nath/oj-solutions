import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        neg = 0
        ok = True
        for i in range(n):
            if ls[i] < 0:
                neg += 1
                ls[i] *= -1

        for i in range(n):
            if neg > 0:
                ls[i] *= -1
                neg -= 1
        
        for i in range(n-1):
            if ls[i] > ls[i+1]:
                ok = False
                break
        
        print("YES" if ok else "NO")
        

if __name__ == "__main__":
    main()
     