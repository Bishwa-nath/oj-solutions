import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n, m = get_ints()
    user = {}
    for i in range(n):
        k, v = input().split()
        user[v] = k
    command = {}
    for i in range(m):
        k, v = input().split()
        x = v[:-1]
        if x in user:
            print("{} {} #{}".format(k, v, user[x]))
    

if __name__ == "__main__":
    main()
    