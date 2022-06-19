import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        m = int(input())
        b = get_ls()
        max_a = max(a)
        max_b = max(b)
        if max_a == max_b:
            print("Alice")
            print("Bob")
        elif max_a < max_b:
            print("Bob")
            print("Bob")
        else:
            print("Alice")
            print("Alice")

if __name__ == "__main__":
    main()
     