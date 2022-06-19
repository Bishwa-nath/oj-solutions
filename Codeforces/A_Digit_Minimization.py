import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        if len(s) == 2:
            print(s[1])
        else:
            ls = []
            for i in s:
                x = int(i)
                ls.append(x)
            print(min(ls))

if __name__ == "__main__":
    main()
     