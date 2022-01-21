import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        st = set()
        ls = get_ls()
        for x in ls:
            while((x > n or x in st) and x > 1):
                x >>= 1
            st.add(x)

        print("YES" if len(st) == n else "NO")


if __name__ == "__main__":
    main()
