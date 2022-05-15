import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, m = get_ints()
        s = []
        for i in range(n):
            x = input()
            s.append(list(x))
        for i in range(m):
            for k in range(n):
                for j in range(n-1, 0, -1):
                    if s[j][i] == '.' and s[j-1][i] == '*':
                        s[j][i], s[j-1][i] = s[j-1][i], s[j][i]
        for k in s:
            print("".join(k))
        print()
        

if __name__ == "__main__":
    main()
    