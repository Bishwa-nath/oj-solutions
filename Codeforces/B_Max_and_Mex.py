import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, k = get_ints()
        ls = get_ls()
        st = set(ls)
        ax = max(ls)
        ex = 0
        for i in range(ax+2):
            if i not in st:
                ex = i
                break
        if ex == ax+1:
            print(n+k)
            continue
        if k> 0:
            st.add((ax+ex+1)//2)
        print(len(st))

    

if __name__ == "__main__":
    main()
    