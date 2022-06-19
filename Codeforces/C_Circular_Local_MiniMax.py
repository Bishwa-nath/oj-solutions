import sys, math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_ls()
        a.sort(reverse=True)
        i = 0
        j = n-1
        ls = []
        while i <= j:
            if i < j:
                ls.append(a[i])
                ls.append(a[j])
            elif i == j and n%2 == 1:
                ls.append(a[i])
            i += 1
            j -= 1

        ok = True
        for i in range(1, n-1):
            if (ls[i-1] > ls[i] < ls[i+1]) or (ls[i-1] < ls[i] > ls[i+1]):
                ok = True
            else:
                ok = False
                break

        if ok:
            print("YES")
            print(*ls)
        else:
            print("NO")
        


if __name__ == "__main__":
    main()
     