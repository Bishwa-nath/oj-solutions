import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n, x, y = map(int, input().split())
        ls = get_ls()
        for i in ls:
            x ^= i
        print("Alice" if x%2 == y%2 else "Bob")
    

if __name__ == "__main__":
    main()
    