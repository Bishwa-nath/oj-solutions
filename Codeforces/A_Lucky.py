import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        a = 0
        b = 0
        for i in range(3):
            a += int(s[i])
        for i in range(3, 6):
            b += int(s[i])
        if a== b:
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
     