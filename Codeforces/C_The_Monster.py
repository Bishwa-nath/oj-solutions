import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    s = input()
    ans, n = 0, len(s)
    for i in range(n-1):
        j, a, q = i, 0, 0
        while j<n and a+q >=0:
            a += s[j] == "("
            a -= s[j] == ")"
            q += s[j] == "?"
            if a < q:
                a, q = q, a
            if a==q: ans += 1
            j += 1
    print(ans)
    

if __name__ == "__main__":
    main()
    