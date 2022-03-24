import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        odd = []
        even = []
        for x in ls:
            if x%2 == 0:
                even.append(x)
            else: odd.append(x)

        t1 = odd.copy()
        t2 = even.copy()
        t1.sort()
        t2.sort()
        if t1 == odd and t2 == even:
            print("Yes")
        else: print("No")
    

if __name__ == "__main__":
    main()
    