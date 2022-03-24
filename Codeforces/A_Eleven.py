import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    
    n = int(input())
    a = 0
    b = 1
    st = set()
    st.add(b)
    while a < n:
        a, b = a+b, a
        st.add(a)
    
    for i in range(1, n+1):
        if i in st:
            print("O", end='')
        else: print("o", end='')
    print()
    

if __name__ == "__main__":
    main()
    